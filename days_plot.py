# Author: LiquidFun
# Source: https://github.com/LiquidFun/adventofcode

import itertools
from collections import namedtuple
from dataclasses import dataclass
from functools import cache
from pathlib import Path
import re

import requests
from PIL import Image, ImageColor
import yaml
from PIL.ImageDraw import ImageDraw
from PIL import ImageFont

DEBUG = False

YEAR_PATTERN = r"\d{4}"
DAY_PATTERN = r"\d{2}"

self_leaderboard_url = "https://adventofcode.com/{year}/leaderboard/self"

aoc_folder = Path("__file__").absolute().parent
cache_path = aoc_folder / ".cache"

DayScores = namedtuple("DayScores", ["time1", "rank1", "score1", "time2", "rank2", "score2"], defaults=[None] * 3)

not_completed_color = ImageColor.getrgb("#333333")


def get_extension_to_colors():
    extension_to_color = {}
    with open(aoc_folder / "Media/github_languages.yml", "r") as file:
        github_languages = yaml.load(file, Loader=yaml.FullLoader)
        for language, data in github_languages.items():
            if "color" in data and "extensions" in data:
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


def request_leaderboard(year) -> dict[str, DayScores]:
    leaderboard_path = cache_path / f"leaderboard{year}.html"
    if leaderboard_path.exists():
        leaderboard = parse_leaderboard(leaderboard_path)
        has_no_none_values = all(itertools.chain(map(list, leaderboard.values())))
        if has_no_none_values:
            return leaderboard
    with open("session.cookie") as cookie_file:
        session_cookie = cookie_file.read().strip()
        data = requests.get(self_leaderboard_url.format(year=year), cookies={"session": session_cookie}).text
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
    return (c[0] - 10, c[1] - 10, c[2] - 10, 255)


def get_alternating_background(languages, both_parts_completed=True, *, stripe_width=20):
    colors = [ImageColor.getrgb(extension_to_color[language]) for language in languages]
    if len(colors) == 1:
        colors.append(darker_color(colors[0]))
    image = Image.new("RGB", (200, 100), not_completed_color)

    def fill_with_colors(colors, fill_only_half):
        for x in range(image.width):
            for y in range(image.height):
                if fill_only_half and x / image.width + y / image.height > 1:
                    continue
                image.load()[x, y] = colors[((x + y) // stripe_width) % len(colors)]

    fill_with_colors([not_completed_color, darker_color(not_completed_color)], False)
    if colors:
        fill_with_colors(colors, not both_parts_completed)
    return image


@cache
def get_font(name: str, size: int):
    return ImageFont.truetype(name, size)


def fmt_time(time: str) -> str:
    time = time.replace("&gt;", ">")
    if ">" in time:
        formatted = time
    else:
        h, m, s = time.split(":")
        formatted = f">{h}h" if int(h) >= 1 else f"{m:02}:{s:02}"
    return f"{formatted:>5}"


def gen_day_graphic(day: str, year: str, languages: list[str], day_scores: DayScores | None) -> Path:
    image = get_alternating_background(languages, not (day_scores is None or day_scores.time2 is None))
    drawer = ImageDraw(image)
    paytone = lambda size: get_font("Media/fonts/PaytoneOne.ttf", size)
    source_code = lambda size: get_font("Media/fonts/SourceCodePro-Regular.otf", size)
    drawer.text((1, -10), str(day), fill="white", align="center", font=paytone(75))
    lang_as_str = ' '.join(languages)
    lang_font_size = max(6, int(18 - max(0, len(lang_as_str) - 8) * 1.3))
    drawer.text((0, 74), lang_as_str, fill="white", align="left", font=source_code(lang_font_size))
    drawer.text((3, -5), "Day", fill="white", align="left", font=paytone(20))

    # drawer.text((123, 0), f"LoC:{loc:3}", fill="white", align="right", font=source_code(18))

    if day_scores is not None and day_scores.time1 is not None:
        drawer.text((104, -5), "P1 ", fill="white", align="left", font=paytone(25))
        drawer.text((105, 25), "time", fill="white", align="right", font=source_code(8))
        drawer.text((105, 35), "rank", fill="white", align="right", font=source_code(8))
        drawer.text((143, 3), fmt_time(day_scores.time1), fill="white", align="right", font=source_code(18))
        drawer.text((143, 23), f"{day_scores.rank1:>5}", fill="white", align="right", font=source_code(18))
    else:
        drawer.line((140, 15, 160, 35), fill="white", width=2)
        drawer.line((140, 35, 160, 15), fill="white", width=2)
    if day_scores is not None and day_scores.time2 is not None:
        drawer.text((104, 45), "P2 ", fill="white", align="left", font=paytone(25))
        drawer.text((105, 75), "time", fill="white", align="right", font=source_code(8))
        drawer.text((105, 85), "rank", fill="white", align="right", font=source_code(8))
        drawer.text((143, 53), fmt_time(day_scores.time2), fill="white", align="right", font=source_code(18))
        drawer.text((143, 73), f"{day_scores.rank2:>5}", fill="white", align="right", font=source_code(18))
    else:
        drawer.line((140, 65, 160, 85), fill="white", width=2)
        drawer.line((140, 85, 160, 65), fill="white", width=2)

    if day_scores is None:
        drawer.line((10, 85, 70, 85), fill="white", width=2)
    drawer.line((100, 5, 100, 95), fill="white", width=1)
    drawer.line((105, 50, 195, 50), fill="white", width=1)

    path = aoc_folder / f"Media/{year}/{day}.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path)
    return path


def handle_day(day_path: Path, html: HTML, day_scores: DayScores | None):
    languages = []
    solution_file_path = None
    loc = 0
    for file_path in day_path.glob("*"):
        if file_path.is_file():
            if file_path.suffix.lower() in extension_to_color:
                if solution_file_path is None:
                    solution_file_path = file_path.relative_to(aoc_folder)
                    loc = solution_file_path.open().read().count("\n")
                languages.append(file_path.suffix.lower())
    languages = list(set(languages))
    if DEBUG:
        if day_path.name == "25":
            languages = []
    day_graphic_path = gen_day_graphic(day_path.name, day_path.parent.name, languages, day_scores)
    day_graphic_path = day_graphic_path.relative_to(aoc_folder)
    with html.tag("td"):
        with html.tag("a", href=str(solution_file_path)):
            html.tag("img", closing=False, src=str(day_graphic_path))


def handle_year(year_path: Path):
    leaderboard = request_leaderboard(year_path.name)
    if DEBUG:
        leaderboard["25"] = None
        leaderboard["24"] = DayScores("22:22:22", "12313", "0")
    html = HTML()
    with html.tag("h1", align="center"):
        html.push(f"{year_path.name}")
    with html.tag("table"):
        for day in range(1, 26, 5):
            with html.tag("tr"):
                for row in range(5):
                    day_str = f"{day + row:02}"
                    day_path = year_path / day_str
                    if day_path.exists():
                        handle_day(day_path, html, leaderboard.get(str(day + row), None))
    with open("README.md", "r") as file:
        text = file.read()

        begin = "<!-- REPLACE FROM -->"
        end = "<!-- REPLACE UNTIL -->"
        pattern = re.compile(rf"{begin}.*{end}", re.DOTALL | re.MULTILINE)
        new_text = pattern.sub(f"{begin}\n{html}\n{end}", text)
    with open("README.md", "w") as file:
        file.write(str(new_text))


def main():
    for year_path in get_paths_matching_regex(aoc_folder, YEAR_PATTERN):
        print(f"Generating table for year {year_path.name}")
        handle_year(year_path)


if __name__ == '__main__':
    main()
