"""
Author: LiquidFun
Source: https://github.com/LiquidFun/adventofcode

To use this script, you need to have a file named
"session.cookie" in the same folder as this script.

It should contain a single line, the "session" cookie
when logged in to https://adventofcode.com. Just
paste it in there.

Then install the requirements as listed in the requirements.txt:
    pip install -r requirements.txt

Then run the script:
    python create_aoc_tiles.py
"""
import itertools
import math
from collections import namedtuple
from functools import cache
from pathlib import Path
import re

import requests
from PIL import Image, ImageColor
import yaml
from PIL.ImageDraw import ImageDraw
from PIL import ImageFont


# The year and day pattern to detect directories. For example, if your day folders are
# called "day1" to "day25" then set the pattern to r"day\d{1,2}". The script extracts
# a number from the folder and tries to guess its day that way.
YEAR_PATTERN = r"\d{4}"
DAY_PATTERN = r"\d{2}"

# 161px is a rather specific number, with it exactly 5 tiles fit into a row. It is possible to go
# to 162px, however then 1080p displays show 4 tiles in a row, and phone displays show 1 tile
# instead of 2 in a row. Therefore, 161px is used here.
TILE_WIDTH_PX = "161px"


NOT_COMPLETED_COLOR = ImageColor.getrgb("#333333")


# This results in the parent folder of the script, the year folders should be here
AOC_FOLDER = Path("__file__").absolute().parent

# Cache path is a subfolder of the AOC folder, it includes the personal leaderboards for each year
CACHE_PATH = AOC_FOLDER / ".cache"

# === The following do not need to be changed ===
# Overrides day 24 part 2 and day 25 both parts to be unsolved
DEBUG = False

# URL for the personal leaderboard (same for everyone)
PERSONAL_LEADERBOARD_URL = "https://adventofcode.com/{year}/leaderboard/self"

DayScores = namedtuple("DayScores", ["time1", "rank1", "score1", "time2", "rank2", "score2"], defaults=[None] * 3)



def get_extension_to_colors():
    extension_to_color = {}
    with open(AOC_FOLDER / "Media/github_languages.yml", "r") as file:
        github_languages = yaml.load(file, Loader=yaml.FullLoader)
        for language, data in github_languages.items():
            if "color" in data and "extensions" in data and data["type"] == "programming":
                for extension in data["extensions"]:
                    extension_to_color[extension.lower()] = data["color"]
    return extension_to_color


extension_to_color: dict[str, str] = get_extension_to_colors()


def get_paths_matching_regex(path: Path, pattern: str):
    return sorted([p for p in path.iterdir() if re.fullmatch(pattern, p.name)])


def parse_leaderboard(leaderboard_path: Path) -> dict[str, DayScores]:
    no_stars = "You haven't collected any stars... yet."
    start = '<span class="leaderboard-daydesc-both">    Time   Rank  Score</span>\n'
    end = "</pre>"
    with open(leaderboard_path) as file:
        html = file.read()
        if no_stars in html:
            return {}
        matches = re.findall(rf"{start}(.*?){end}", html, re.DOTALL | re.MULTILINE)
        assert len(matches) == 1, f"Found {'no' if len(matches) == 0 else 'more than one'} leaderboard?!"
        table_rows = matches[0].strip().split("\n")
        leaderboard = {}
        for line in table_rows:
            day, *scores = re.split(r"\s+", line.strip())
            assert len(scores) in (3, 6), f"Number scores for {day=} ({scores}) are not 3 or 6."
            leaderboard[day] = DayScores(*scores)
        return leaderboard


def request_leaderboard(year: int) -> dict[str, DayScores]:
    leaderboard_path = CACHE_PATH / f"leaderboard{year}.html"
    if leaderboard_path.exists():
        leaderboard = parse_leaderboard(leaderboard_path)
        has_no_none_values = all(itertools.chain(map(list, leaderboard.values())))
        if has_no_none_values:
            return leaderboard
    with open("session.cookie") as cookie_file:
        session_cookie = cookie_file.read().strip()
        data = requests.get(PERSONAL_LEADERBOARD_URL.format(year=year), cookies={"session": session_cookie}).text
        with open(leaderboard_path, "w") as file:
            file.write(data)
    return parse_leaderboard(leaderboard_path)


class HTMLTag:
    def __init__(self, parent: "HTML", tag: str, closing: bool = True, **kwargs):
        self.parent = parent
        self.tag = tag
        self.closing = closing
        self.kwargs = kwargs
        attributes = ''.join(f' {k}="{v}"' for k, v in self.kwargs.items())
        self.parent.push(f"<{self.tag}{attributes}>", depth=self.closing)

    def __enter__(self):
        pass

    def __exit__(self, *args):
        if self.closing:
            self.parent.push(f"</{self.tag}>", depth=-self.closing)


class HTML:
    tags: list[str] = []
    depth = 0

    def push(self, tag: str, depth=0):
        if depth < 0:
            self.depth += depth
        self.tags.append("  " * self.depth + tag)
        if depth > 0:
            self.depth += depth

    def tag(self, tag: str, closing: bool = True, **kwargs):
        return HTMLTag(self, tag, closing, **kwargs)

    def __str__(self):
        return "\n".join(self.tags)


def darker_color(c: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    return c[0] - 10, c[1] - 10, c[2] - 10, 255


def get_alternating_background(languages, both_parts_completed=True, *, stripe_width=20):
    colors = [ImageColor.getrgb(extension_to_color[language]) for language in languages]
    if len(colors) == 1:
        colors.append(darker_color(colors[0]))
    image = Image.new("RGB", (200, 100), NOT_COMPLETED_COLOR)

    def fill_with_colors(colors, fill_only_half):
        for x in range(image.width):
            for y in range(image.height):
                if fill_only_half and x / image.width + y / image.height > 1:
                    continue
                image.load()[x, y] = colors[((x + y) // stripe_width) % len(colors)]

    fill_with_colors([NOT_COMPLETED_COLOR, darker_color(NOT_COMPLETED_COLOR)], False)
    if colors:
        fill_with_colors(colors, not both_parts_completed)
    return image


@cache
def get_font(name: str, size: int):
    return ImageFont.truetype(str(AOC_FOLDER / name), size)


def fmt_time(time: str) -> str:
    """Formats time as mm:ss if the time is below 1 hour, otherwise it returns >1h to a max of >24h"""
    time = time.replace("&gt;", ">")
    if ">" in time:
        formatted = time
    else:
        h, m, s = time.split(":")
        formatted = f">{h}h" if int(h) >= 1 else f"{m:02}:{s:02}"
    return f"{formatted:>5}"


def draw_star(drawer: ImageDraw, at: tuple[int, int], size=9, color="#ffff0022", num_points=5):
    """Draws a star at the given position"""
    diff = math.pi * 2 / num_points / 2
    points: list[tuple[float, float]] = []
    for angle in [diff * i - math.pi / 2 for i in range(num_points * 2)]:
        factor = size if len(points) % 2 == 0 else size * .4
        points.append((at[0] + math.cos(angle) * factor, at[1] + math.sin(angle) * factor))
    drawer.polygon(points, fill=color)


def gen_day_graphic(day: str, year: str, languages: list[str], day_scores: DayScores | None) -> Path:
    """Saves a graphic for a given day and year. Returns the path to it."""
    image = get_alternating_background(languages, not (day_scores is None or day_scores.time2 is None))
    drawer = ImageDraw(image)
    paytone = lambda size: get_font("Media/fonts/PaytoneOne.ttf", size)
    source_code = lambda size: get_font("Media/fonts/SourceCodePro-Regular.otf", size)
    font_color = "white"

    # === Left side ===
    drawer.text((3, -5), "Day", fill=font_color, align="left", font=paytone(20))
    drawer.text((1, -10), str(day), fill=font_color, align="center", font=paytone(75))
    # Calculate font size based on number of characters, because it might overflow
    lang_as_str = ' '.join(languages)
    lang_font_size = max(6, int(18 - max(0, len(lang_as_str) - 8) * 1.3))
    drawer.text((0, 74), lang_as_str, fill=font_color, align="left", font=source_code(lang_font_size))

    # === Right side (P1 & P2) ===
    for part in (1, 2):
        time, rank = getattr(day_scores, f"time{part}"), getattr(day_scores, f"rank{part}")
        y = 50 if part == 2 else 0
        if day_scores is not None and time is not None:
            drawer.text((104, -5 + y), f"P{part} ", fill=font_color, align="left", font=paytone(25))
            drawer.text((105, 25 + y), "time", fill=font_color, align="right", font=source_code(10))
            drawer.text((105, 35 + y), "rank", fill=font_color, align="right", font=source_code(10))
            drawer.text((143, 3 + y), fmt_time(time), fill=font_color, align="right", font=source_code(18))
            drawer.text((133, 23 + y), f"{rank:>6}", fill=font_color, align="right", font=source_code(18))
        else:
            drawer.line((140, 15 + y, 160, 35 + y), fill=font_color, width=2)
            drawer.line((140, 35 + y, 160, 15 + y), fill=font_color, width=2)

    if day_scores is None:
        drawer.line((10, 85, 70, 85), fill=font_color, width=2)

    # === Divider lines ===
    drawer.line((100, 5, 100, 95), fill=font_color, width=1)
    drawer.line((105, 50, 195, 50), fill=font_color, width=1)

    path = AOC_FOLDER / f"Media/{year}/{day}.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path)
    return path


def handle_day(day: int, year: int, day_path: Path, html: HTML, day_scores: DayScores | None):
    languages = []
    solution_file_path = None
    if day_path is not None:
        for file_path in day_path.glob("*"):
            if file_path.is_file():
                if file_path.suffix.lower() in extension_to_color:
                    if solution_file_path is None:
                        solution_file_path = file_path.relative_to(AOC_FOLDER)
                    languages.append(file_path.suffix.lower())
    languages = sorted(set(languages))
    if DEBUG:
        if day == 25:
            languages = []
    day_graphic_path = gen_day_graphic(f"{day:02}", f"{year:04}", languages, day_scores)
    day_graphic_path = day_graphic_path.relative_to(AOC_FOLDER)
    with html.tag("a", href=str(solution_file_path)):
        html.tag("img", closing=False, src=str(day_graphic_path), width=TILE_WIDTH_PX)


def find_first_number(string: str) -> int:
    return int(re.findall(r"\d+", string)[0])


def handle_year(year_path: Path, year: int):
    leaderboard = request_leaderboard(year)
    if DEBUG:
        leaderboard["25"] = None
        leaderboard["24"] = DayScores("22:22:22", "12313", "0")
    html = HTML()
    with html.tag("h1", align="center"):
        html.push(f"{year}")
    days_with_filled_gaps = {find_first_number(p.name): p for p in get_paths_matching_regex(year_path, DAY_PATTERN)}
    if len(days_with_filled_gaps) == 0:
        print(f"Year {year} is empty!")
        return
    max_day = max(*days_with_filled_gaps, *map(int, leaderboard))
    for day in range(1, max_day + 1):
        if day not in days_with_filled_gaps:
            days_with_filled_gaps[day] = None
    for day, day_path in days_with_filled_gaps.items():
        handle_day(day, year, day_path, html, leaderboard.get(str(day), None))

    with open("README.md", "r") as file:
        text = file.read()
        begin = "<!-- AOC TILES BEGIN -->"
        end = "<!-- AOC TILES END -->"
        pattern = re.compile(rf"{begin}.*{end}", re.DOTALL | re.MULTILINE)
        new_text = pattern.sub(f"{begin}\n{html}\n{end}", text)

    with open("README.md", "w") as file:
        file.write(str(new_text))


def main():
    for year_path in sorted(get_paths_matching_regex(AOC_FOLDER, YEAR_PATTERN), reverse=True):
        year = find_first_number(year_path.name)
        print(f"=== Generating table for year {year} ===")
        handle_year(year_path, year)


if __name__ == '__main__':
    main()
