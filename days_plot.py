from dataclasses import dataclass
from pathlib import Path
import re

from PIL import Image
import yaml
from PIL.ImageDraw import ImageDraw
from PIL import ImageFont

YEAR_PATTERN = r"\d{4}"
DAY_PATTERN = r"\d{2}"


def get_paths_matching_regex(path: Path, pattern: str):
    return sorted([p for p in path.iterdir() if re.fullmatch(pattern, p.name)])


aoc_folder = Path("__file__").absolute().parent
years = get_paths_matching_regex(aoc_folder, YEAR_PATTERN)

extension_to_color = {}

with open(aoc_folder / "Media/github_languages.yml", "r") as file:
    github_languages = yaml.load(file, Loader=yaml.FullLoader)
    for language, data in github_languages.items():
        if "color" in data and "extensions" in data:
            for extension in data["extensions"]:
                extension_to_color[extension.lower()] = data["color"]

print(extension_to_color)

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


def gen_day_graphic(day: str, year: str, languages: list[str], loc: int) -> Path:
    color = extension_to_color[languages[0]] if languages else "#333333"
    image = Image.new("RGB", (200, 100), color)
    drawer = ImageDraw(image)
    main_font = ImageFont.truetype("Media/fonts/PaytoneOne.ttf", 98)
    side_font = ImageFont.truetype("Media/fonts/SourceCodePro-Regular.otf", 17)
    drawer.text((0, -40), str(day), fill="white", align="center", font=main_font)
    drawer.text((0, 74), ' '.join(languages), fill="white", align="left", font=side_font)

    drawer.text((123, 0), f"LoC:{loc:3}", fill="white", align="right", font=side_font)
    path = aoc_folder / f"Media/{year}/{day}.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path)
    return path


def handle_day(day_path: Path, html: HTML):
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
    day_graphic_path = gen_day_graphic(day_path.name, day_path.parent.name, languages, loc)
    day_graphic_path = day_graphic_path.relative_to(aoc_folder)
    with html.tag("td"):
        with html.tag("a", href=str(solution_file_path)):
            html.tag("img", closing=False, src=str(day_graphic_path))


def handle_year(year_path: Path):
    html = HTML()
    with html.tag("table"):
        print(year_path)
        for day in range(1, 26, 5):
            with html.tag("tr"):
                for row in range(5):
                    day_str = f"{day+row:02}"
                    day_path = year_path / day_str
                    if day_path.exists():
                        handle_day(day_path, html)
    print(html)
    with open("README.md", "r") as file:
        text = file.read()

        begin = "<!-- REPLACE FROM -->"
        end = "<!-- REPLACE UNTIL -->"
        pattern = re.compile(rf"{begin}.*{end}", re.DOTALL | re.MULTILINE)
        print(pattern)
        new_text = pattern.sub(f"{begin}\n{html}\n{end}", text)
    with open("README.md", "w") as file:
        print(new_text)
        file.write(str(new_text))


def main():
    for year in years:
        print(year)
        handle_year(year)


if __name__ == '__main__':
    main()
