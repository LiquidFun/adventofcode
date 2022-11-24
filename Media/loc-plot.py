#!/usr/bin/python3

import argparse
from pathlib import Path
from datetime import datetime
from collections import Counter

from matplotlib import pyplot as plt

directory = Path(__file__).parent

def get_languages_used(path: Path):
    """ Returns (count, language) tuples, e.g.: [(1, '.apl'), (3, '.py'), (24, '.jl')] """
    ignore = [".in", ".run", ".sh", ".ans", "", ".cookie"]
    occ = Counter(file.suffix for file in path.glob("**/*") if file.suffix not in ignore)
    return sorted(zip(occ.values(), occ.keys()))

def make_plot_for_year(year: int, lang="auto"):
    year_dir = directory / str(year)
    if lang == "auto":
        lang = get_languages_used(year_dir)[-1][1]
    if lang[0] != '.':
        lang = f".{lang}"

    loc = []
    for day_dir in filter(lambda p: p.is_dir(), year_dir.iterdir()):
        names = [f"{day_dir.name}", f"{int(day_dir.name)}"]
        for name in names:
            if (filepath := day_dir / f"{name}{lang}").exists():
                with open(filepath, "r") as file:
                    lines = [*filter(lambda line: line.strip() != "", file.read().strip().split("\n"))]
                    loc.append(len(lines))
                    break
    xticks = [*range(1, len(loc)+1)]
    bars = plt.bar(xticks, loc)
    for bar, line_count in zip(bars, loc):
        plt.text(bar.get_x() + .45, line_count + 1, line_count, ha="center")
    plt.title(f"Lines of code for each '{lang}' solution in Advent of Code {year}")
    plt.xticks(xticks)
    plt.yticks(range(0, 130, 10))
    plt.ylabel("Lines of code")
    plt.xlabel("Day")
    # plt.show()
    plt.savefig(directory / "Media" / f"{year}loc.png")
    

def main():
    date = datetime.now()
    year = date.year - (date.month <= 11)
    parser = argparse.ArgumentParser("Make fancy plot (not really)")
    parser.add_argument("-y", "--year", default=year)
    parser.add_argument("-l", "--lang", default="auto")
    parsed = parser.parse_args()

    make_plot_for_year(parsed.year, parsed.lang)


if __name__ == "__main__":
    main()
