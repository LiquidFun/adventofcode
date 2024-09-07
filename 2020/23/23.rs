use std::io::stdin;

use itertools::Itertools;

fn solve(initial: Vec<usize>, steps: i32) -> Vec<usize> {
    let mut cups = initial.iter().zip(initial.iter().cycle().skip(1)).sorted().map(|a| a.1).copied().collect_vec();
    cups.insert(0, 0);
    let mut curr = initial[0];
    let max = initial.len();

    for _ in 0..steps {
        let first = cups[curr];
        let second = cups[first];
        let third = cups[second];

        let mut dest = curr;
        while [curr, first, second, third].contains(&dest) { dest = (dest + max - 2) % max + 1 }

        cups[curr] = cups[third];
        cups[third] = cups[dest];
        cups[dest] = first;

        curr = cups[curr];
    }

    let mut sorted = Vec::new();
    curr = 1;
    for _ in 0..max {
        sorted.push(curr);
        curr = cups[curr];
    }
    sorted
}

fn main() {
    let cups = stdin().lines().next().unwrap().unwrap().chars().map(|c| c.to_digit(10).unwrap() as usize).collect_vec();
    println!("{}", solve(cups.clone(), 100).iter().skip(1).join(""));

    let p2 = cups.into_iter().chain(10..=1_000_000).collect();
    println!("{}", solve(p2, 10_000_000).into_iter().skip(1).take(2).reduce(|acc, a| acc * a).unwrap());
}