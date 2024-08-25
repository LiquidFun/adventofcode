use std::{collections::HashSet, io::stdin};

use itertools::{iproduct, Itertools};

fn adjacent(p: &Vec<i32>) -> HashSet<Vec<i32>> {
    let r = [-1, 0, 1];

    match p.len() {
        3 => iproduct!(r, r, r)
            .map(|(dx, dy, dz)| vec![p[0] + dx, p[1] + dy, p[2] + dz])
            .collect(),
        4 => iproduct!(r, r, r, r)
            .map(|(dx, dy, dz, dw)| vec![p[0] + dx, p[1] + dy, p[2] + dz, p[3] + dw])
            .collect(),
        _ => HashSet::new(),
    }
}

fn solve(initial_active: HashSet<Vec<i32>>) {
    let mut active = initial_active;
    for _ in 0..6 {
        let mut new_active = HashSet::new();
        let mut inactive = HashSet::new();
        for xyz in active.iter() {
            let adj = adjacent(xyz);
            inactive.extend(adj.difference(&active).cloned());
            if (3..=4).contains(&adj.intersection(&active).count()) {
                new_active.insert(xyz.to_vec());
            }
        }
        for xyz in inactive.iter() {
            if adjacent(xyz).intersection(&active).count() == 3 {
                new_active.insert(xyz.to_vec());
            }
        }
        active = new_active;
    }
    println!("{:?}", active.len());
}

fn main() {
    let active = stdin()
        .lines()
        .enumerate()
        .map(|(y, line)| {
            line.unwrap()
                .chars()
                .enumerate()
                .filter(|(_, c)| *c == '#')
                .map(|(x, _)| vec![y as i32, x as i32, 0])
                .collect_vec()
        })
        .flatten()
        .collect::<HashSet<_>>();
    solve(active.clone());
    solve(active.iter().map(|v| v.iter().cloned().chain(vec![4]).collect()).collect());
}