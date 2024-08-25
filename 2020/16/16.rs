use std::{collections::HashSet, io::stdin};

use hopcroft_karp::matching;
use itertools::Itertools;
use regex::Regex;

fn main() {
    let raw_input = stdin().lines().filter_map(Result::ok).join("\n");
    let input = raw_input.split("\n\n").collect_vec();
    let pattern = Regex::new(r"\d+").unwrap();
    let mut sum = 0;

    let ranges = input
        .get(0)
        .unwrap()
        .split("\n")
        .map(|line| {
            pattern
                .find_iter(line)
                .map(|a| a.as_str().parse::<usize>().unwrap())
                .tuple_windows()
                .exactly_one()
                .map(|(a, b, c, d)| (a..=b, c..=d))
                .unwrap()
        })
        .collect_vec();

    let mut allowed: HashSet<(usize, usize)> = (0..ranges.len())
        .cartesian_product(20..ranges.len() + 20)
        .collect();

    for nearby in input.get(2).unwrap().split("\n").skip(1) {
        for (i, num) in nearby
            .split(",")
            .map(|n| n.parse::<usize>().unwrap())
            .enumerate()
        {
            let invalid = ranges
                .iter()
                .map(|(r1, r2)| r1.contains(&num) || r2.contains(&num))
                .all(|n| n == false);
            if invalid {
                sum += num;
            } else {
                ranges
                    .iter()
                    .enumerate()
                    .filter(|(_, (r1, r2))| !(r1.contains(&num) || r2.contains(&num)))
                    .for_each(|(j, _)| {
                        allowed.remove(&(j, i + 20));
                    });
            }
        }
    }
    println!("{:?}", sum);

    let departure_indices = matching(&allowed.clone().into_iter().collect_vec())
        .iter()
        .sorted()
        .take(6)
        .map(|(_, b)| b - 20)
        .collect_vec();

    pattern
        .find_iter(input.get(1).unwrap())
        .map(|a| a.as_str().parse::<usize>().unwrap())
        .enumerate()
        .filter(|(i, _)| departure_indices.contains(i))
        .map(|a| a.1)
        .reduce(|a, b| a * b)
        .map(|a| println!("{:?}", a));
}
