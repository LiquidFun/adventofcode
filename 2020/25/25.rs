use std::io::stdin;
use itertools::Itertools;

fn main() {
    let (card, door) = stdin().lines().map(|n| n.unwrap().parse()).filter_map(Result::ok).next_tuple().unwrap();
    let mut value: usize = 1;
    let card_loop = (0..).map(|_| { value = value * 7 % 20201227; value }).take_while(|v| *v != card).count() + 1;
    println!("{}", (0..card_loop).fold(1, |acc, _| acc * door % 20201227));
}