use std::{collections::HashMap, io::stdin};

use itertools::Itertools;

fn eval(line: &str, plus_precedence: i32) -> i64 {
    let mut nums = Vec::new();
    let mut operators = Vec::new();
    let precedence = HashMap::from([('(', 10), ('+', plus_precedence), ('*', 1)]);
    // eprintln!("line = {:?}", line);
    for c in line.chars().chain(")".chars()) {
        // eprintln!("c = {:?}, nums = {:?}, ops = {:?}", c, nums, operators);
        match c {
            '0'..='9' => nums.push(c.to_digit(10).unwrap() as i64),
            '(' =>  operators.push(c),
            ')' => {
                while !operators.is_empty() {
                    let op = operators.pop().unwrap();
                    if op == '(' {
                        break;
                    }
                    let func = if op == '*' { |(a, b)| a * b } else { |(a, b)| a + b };
                    let value = nums.pop().zip(nums.pop()).map(func).unwrap();
                    nums.push(value);
                }
            }
            '+' | '*' => {
                while !operators.is_empty() {
                    // eprintln!("\tc = {:?}, nums = {:?}, ops = {:?}", c, nums, operators);
                    let op = operators.last().unwrap();
                    if *op == '(' || precedence.get(op).unwrap() < precedence.get(&c).unwrap() {
                        break;
                    }
                    let func = if *op == '*' { |(a, b)| a * b } else { |(a, b)| a + b };
                    let value = nums.pop().zip(nums.pop()).map(func).unwrap();
                    nums.push(value);
                    operators.pop();
                }
                operators.push(c);
            },
            _ => (),
        }
    }
    *nums.get(0).unwrap()
}

fn main() {
    let lines = stdin() .lines().filter_map(Result::ok).collect_vec();
    println!("{:?}", lines.iter().map(|l| eval(&l, 1)).sum::<i64>()); 
    println!("{:?}", lines.iter().map(|l| eval(&l, 2)).sum::<i64>()); 
}
