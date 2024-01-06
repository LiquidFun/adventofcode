use std::io::stdin;

use itertools::Itertools;

fn as_binary(s: &str) -> i32 {
    s.char_indices().fold(0, |acc, (i, c)| acc + (1<<(9-i)) * ("BR".contains(c) as i32))
}

fn main() {
    let nums: Vec<i32> = stdin().lines().map(|l| as_binary(&l.unwrap())).collect();
    println!("{:?}", nums.iter().max().unwrap());
    nums.iter()
        .sorted()
        .tuple_windows()
        .find(|(&a, &b)| b-a == 2)
        .map(|(&a, _)| println!("{}", a+1));
}
