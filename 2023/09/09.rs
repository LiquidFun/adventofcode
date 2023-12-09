use std::io::{stdin, Read};
use itertools::Itertools;

fn main() {
    let mut input = String::new();
    stdin().read_to_string(&mut input).unwrap();

    let mut first = 0;
    let mut last = 0;
    for line in input.lines() {
        let mut diff = line.split(' ').map(|n| n.parse().unwrap()).collect::<Vec<i32>>();
        let mut sign = 1;
        while let [a, .., z] = *diff {
            first += a * sign;
            last += z;
            sign *= -1;
            diff = diff.iter().tuple_windows().map(|(a, b)| b - a).collect();
        }
    }
    println!("{}\n{}", last, first);
}