#!/usr/bin/bash

year="2023"
cookie=$(cat session.cookie)
input_prefix="input"
sample_prefix="example"

# Example comes before input alphabetically, so it shows up in front in the program-tester.sh

if [[ "$1" ]]; then
    if ! [[ -d "$1" ]]; then
	echo "Creating folder for problem $1"
	mkdir "$1"
    fi
    cd "$1"

    # Download input from advent of code
    input_file="${input_prefix}.in"
    if ! [[ -f "$input_file" ]]; then
	echo "Downloading input for problem $1"
	# Don't DDOS! So check if file exists already
	nozero=$(echo "$1" | awk '$0*=1')
	curl "https://adventofcode.com/$year/day/$nozero/input" --cookie "session=$cookie" > "$input_file"
    fi

    # Add empty file so there are not that many lines when showing input instead
    input_ans_file="${input_prefix}.ans"
    if ! [[ -f "$input_ans_file" ]]; then
	echo "Create empty input answer file"
	touch "$input_ans_file"
    fi

    # Prepare dummy python solution
    solution_file="$1.py"
    if ! [[ -f "$solution_file" ]]; then
	echo "Create dummy python solution $solution_file"
	cp "../../dummy.py" "$solution_file"
    fi


    nvim "$solution_file" "${sample_prefix}.in" "${sample_prefix}.ans" -c "norm G$"
else
    echo "Supply some number as first argument to initialize a problem!"
fi
