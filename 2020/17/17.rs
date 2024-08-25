use std::{collections::HashSet, io::stdin};

use itertools::Itertools;

fn adjacent(xyz: (i32, i32, i32, i32)) -> HashSet<(i32, i32, i32, i32)> {
    (-1..=1)
        .cartesian_product(-1..=1)
        .cartesian_product(-1..=1)
        .cartesian_product(-1..=1)
        .map(|(((x, y), z), w)| (x + xyz.0, y + xyz.1, z + xyz.2, w+xyz.3))
        .collect()
}

fn main() {
    let mut active = stdin()
        .lines()
        .enumerate()
        .map(|(y, line)| {
            line.unwrap()
                .chars()
                .enumerate()
                .filter(|(_, c)| *c == '#')
                .map(|(x, _)| (y as i32, x as i32, 0, 0))
                .collect_vec()
        })
        .flatten()
        .collect::<HashSet<_>>();
    println!("{:?}", active);

    println!("{:?}", active.len());
    for _ in 0..6 {
        let mut new_active = HashSet::new();
        let mut inactive = HashSet::new();
        for xyz in active.iter() {
            inactive.extend(adjacent(*xyz).difference(&active));
            if (3..=4).contains(&adjacent(*xyz).intersection(&active).count()) {
                new_active.insert(*xyz);
            }
        }
        for xyz in inactive.iter() {
            if adjacent(*xyz).intersection(&active).count() == 3 {
                new_active.insert(*xyz);
            }
        }
        active = new_active;
        println!("{:?}", active.len());
    }
}
