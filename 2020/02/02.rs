use itertools::Itertools;
use std::io::stdin;

struct PasswordPhilosophy {
    range: std::ops::RangeInclusive<usize>,
    letter: char,
    string: String,
}

fn get_password_philosophies() -> Vec<PasswordPhilosophy> {
    let lines = stdin().lines().filter_map(Result::ok).collect_vec();
    lines.iter()
        .map(|line| line.split(|c| "- :".contains(c)).next_tuple().unwrap())
        .map(|(a, b, letter, _, string)| {
            PasswordPhilosophy {
                range: a.parse().unwrap()..=b.parse().unwrap(),
                letter: letter.chars().next().unwrap(),
                string: string.to_owned(),
            }
        })
        .collect()
}

fn main() {
    let philosophies = get_password_philosophies();
    println!("{}", philosophies.iter().filter(|p| p.range.contains(&p.string.matches(p.letter).count())).count());

    let sum2 = philosophies
        .iter()
        .filter(|p| {
            let is_first = p.string.chars().nth((p.range.start() - 1) as usize).unwrap() == p.letter;
            let is_second = p.string.chars().nth((p.range.end() - 1) as usize).unwrap() == p.letter;
            is_first != is_second
        })
        .count();

    println!("{}", sum2);
}