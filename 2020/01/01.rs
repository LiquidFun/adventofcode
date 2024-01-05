use std::io::stdin;
use itertools::iproduct;

fn main() {
    let nums: Vec<i32> = stdin().lines().map(|a| a.unwrap().parse::<i32>().unwrap()).collect();    
    iproduct!(&nums, &nums)
        .find(|(&a, &b)| a+b == 2020)
        .map(|(&a, &b)| println!("{}", a*b));
    iproduct!(&nums, &nums, &nums)
        .find(|(&a, &b, &c)| a+b+c == 2020)
        .map(|(&a, &b, &c)| println!("{}", a*b*c));
}