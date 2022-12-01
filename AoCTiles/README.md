# AoC Tiles

This script creates a graphic for each day for each year of the Advent of Code. 
A tile is an image which represents both parts of a day, it looks like this:

![AoC Tiles](examples/basic.png)

It uses the personal [AoC Leaderboard](https://adventofcode.com/2021/leaderboard/self) to get the data for each day using your cookie. 

Set the `SHOW_CHECKMARK_INSTEAD_OF_TIME_RANK` flag to True to get this instead:

![AoC Tiles Checkmark](examples/checkmarks.png)

## Installation

Feel free to use it, here is a short description of how to get it working:

Copy this entire folder into your AoC repository. Then install the requirements.

### Requirements

Install at least Python 3.9.

Install requirements:

```
pip install -r requirements.txt
```

### Configuration

To use this script, you need to have a file named "session.cookie" in the same folder as this script.
It should contain a single line, the "session" cookie
when logged in to https://adventofcode.com. Just
paste it in there.

Your year/day script structure likely looks different. You can change the patterns for years and days in the 
[create_aoc_tiles.py](create_aoc_tiles.py) file.

The variables at the top of the script have comments to explain what they do.

To try whether it works you can run the script directly:

```
python3 create_aoc_tiles.py
```

### Pre-commit hook

Add [.pre-commit-config.yaml](/.pre-commit-config.yaml) to your repository and run `pre-commit install` to install the hook.
