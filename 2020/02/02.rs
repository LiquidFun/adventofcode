use regex::Regex;
use std::io::Read;

#[derive(Debug)]
struct PasswordPhilosophy {
    range: std::ops::Range<i32>,
    letter: char,
    string: String,
}

fn get_password_philosophies() -> Vec<PasswordPhilosophy> {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let pattern = Regex::new(r"(\d+)-(\d+) (\w): (\w+)").unwrap();
    let mut philosophies = Vec::new();
    for cap in pattern.captures_iter(&input) {
        let range = cap[1].parse::<i32>().unwrap()..cap[2].parse::<i32>().unwrap()+1;
        let letter = cap[3].chars().next().unwrap();
        philosophies.push(PasswordPhilosophy { range, letter, string: cap[4].to_string() });
    }
    philosophies
}


fn main() {
    let philosophies = get_password_philosophies();
    let mut sum1 = 0;
    for p in &philosophies {
        let letter_count = p.string.matches(p.letter).count();
        if p.range.contains(&(letter_count as i32)) {
            sum1 += 1
        }
    }

    let mut sum2 = 0;
    for p in &philosophies {
        let is_first = p.string.chars().nth((p.range.start-1) as usize).unwrap() == p.letter;
        let is_second = p.string.chars().nth((p.range.end-2) as usize).unwrap() == p.letter;
        if is_first != is_second {
            sum2 += 1
        }
    }

    println!("{}\n{}", sum1, sum2);
}