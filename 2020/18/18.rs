use std::{collections::HashMap, io::stdin};

fn eval(line: &str, plus_precedence: i32) -> i64 {
    let mut nums = Vec::new();
    let mut operators = Vec::new();
    let precedence = HashMap::from([('(', 0), (')', 0), ('+', plus_precedence), ('*', 1)]);

    for c in line.chars().chain(")".chars()) {
        match c {
            '0'..='9' => nums.push(c.to_digit(10).unwrap() as i64),
            '(' | '+' | '*' | ')' => { 
                while !operators.is_empty() && c != '(' {
                    let op = operators.pop().unwrap();
                    if op == '(' && c == ')'  { break }
                    if precedence.get(&op).unwrap() < precedence.get(&c).unwrap() {
                        operators.push(op);
                        break;
                    }
                    let func = if op == '*' { |(a, b)| a * b } else { |(a, b)| a + b };
                    let value = nums.pop().zip(nums.pop()).map(func).unwrap();
                    nums.push(value);
                }
                if c != ')' { operators.push(c); }
            },
            _ => continue,
        }
    }
    *nums.get(0).unwrap()
}

fn main() {
    let lines: Vec<String> = stdin() .lines().filter_map(Result::ok).collect();
    println!("{:?}", lines.iter().map(|l| eval(&l, 1)).sum::<i64>()); 
    println!("{:?}", lines.iter().map(|l| eval(&l, 2)).sum::<i64>()); 
}