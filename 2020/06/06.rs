use std::{io::stdin, collections::HashSet};

fn main() {
    let sets = stdin().lines()
        .map(|l| l.unwrap().chars().collect::<HashSet<_>>())
        .collect::<Vec<_>>();
    let groups = sets
        .split(|set| set.is_empty())
        .collect::<Vec<_>>();

    let p1: usize = groups.iter()
        .map(|s| s.iter().fold(s[0].clone(), |acc, curr| acc.union(curr).cloned().collect()))
        .fold(0, |acc, l| acc+l.len());
    let p2: usize = groups.iter()
        .map(|s| s.iter().fold(s[0].clone(), |acc, curr| acc.intersection(curr).cloned().collect()))
        .fold(0, |acc, l| acc+l.len());

    println!("{}\n{}", p1, p2);
}