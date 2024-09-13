#!/usr/bin/bash

year="2019"
SCRIPT_DIR="$(dirname "$(realpath "$0")")"
cookie="$(cat $SCRIPT_DIR/.aoc_tiles/session.cookie)"
input_prefix="input"
sample_prefix="example"

# Example comes before input alphabetically, so it shows up in front in the program-tester.sh

if [[ "$1" ]]; then
    dir=$(printf "%02d" "$1")
    path="$SCRIPT_DIR/$year/$dir"
    if ! [[ -d "$path" ]]; then
	echo "Creating folder for problem $dir in $path"
	mkdir "$path"
    fi
    cd "$path"

    # Download input from advent of code
    input_file="$path/${input_prefix}.in"
    echo $input_file
    if ! [[ -f "$input_file" ]]; then
	echo "Downloading input for problem $dir"
	# Don't DDOS! So check if file exists already
	nozero=$(echo "$1" | awk '$0*=1')
	curl "https://adventofcode.com/$year/day/$nozero/input" --cookie "session=$cookie" > "$input_file"
    else
	echo "Skipping $dir because input file exists $input_file"
    fi

    # Add empty file so there are not that many lines when showing input instead
	#    input_ans_file="${input_prefix}.ans"
	#    if ! [[ -f "$input_ans_file" ]]; then
	# echo "Create empty input answer file"
	# touch "$input_ans_file"
	#    fi

    # Prepare dummy python solution
	#    solution_file="$1.py"
	#    if ! [[ -f "$solution_file" ]]; then
	# echo "Create dummy python solution $solution_file"
	# cp "../../dummy.py" "$solution_file"
	#    fi


    # nvim "$solution_file" "${sample_prefix}.in" "${sample_prefix}.ans" -c "norm G$"
else
    echo "Supply some number as first argument to initialize a problem!"
fi
