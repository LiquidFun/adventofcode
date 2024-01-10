use std::io::stdin;
use itertools::Itertools;

fn main() {
    let mut nums: Vec<i64> = stdin().lines().map(|line| line.unwrap().parse().unwrap()).collect();
    nums.extend([0, *nums.iter().max().unwrap()+3]);
    let diffs: Vec<_> = nums.iter().sorted().tuple_windows().map(|(a,b)|b-a).collect();
    let counts = diffs.iter().counts();
    let lookup = [1, 1, 2, 4, 7];
    let p2: i64 = diffs .split(|&n| n == 3) .map(|vec| lookup[vec.len()]) .product();
    println!("{}\n{}", counts[&1]*counts[&3], p2);
}