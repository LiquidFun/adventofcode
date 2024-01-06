use std::{io::stdin, collections::HashMap};

use itertools::Itertools;
use regex::Regex;

fn valid_p1(map: &HashMap<&str, &str>) -> bool {
    "byr iyr eyr hgt hcl ecl pid".split(" ").all(|req| map.contains_key(&req))
}

fn valid_p2(map: &HashMap<&str, &str>) -> bool {
    valid_p1(map)
    && (1920..=2002).contains(&map["byr"].parse().unwrap())
    && (2010..=2020).contains(&map["iyr"].parse().unwrap())
    && (2020..=2030).contains(&map["eyr"].parse().unwrap())
    && Regex::new(r"^((1[5-8]\d|19[0123])cm|(59|6\d|7[0-6])in)$").unwrap().is_match(map["hgt"])
    && Regex::new(r"^#[0-9a-f]{6}$").unwrap().is_match(map["hcl"])
    && Regex::new(r"^\d{9}$").unwrap().is_match(map["pid"])
    && "amb blu brn gry grn hzl oth".split(" ").contains(&map["ecl"])
}

fn main() {
    let input = stdin().lines().filter_map(Result::ok).join(" ");
    let passports: Vec<HashMap<&str, &str>> = input
        .split("  ")
        .map(|line| line.split(" ").map(|e| e.split_once(":").unwrap()).collect())
        .collect();
    println!("{}", passports.iter().filter(|h| valid_p1(h)).count());
    println!("{}", passports.iter().filter(|h| valid_p2(h)).count());
} 