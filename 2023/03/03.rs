use std::{io::{stdin, Read}, collections::HashMap};
use regex::Regex;

fn is_valid(y: i32, x: i32, lines: &Vec<&str>) -> bool {
    (0..lines.len() as i32).contains(&y) && (0..lines[y as usize].len() as i32).contains(&x)
}

fn main() {
    let mut input = String::new();
    stdin().read_to_string(&mut input).unwrap();
    let lines = input.trim().split("\n").collect::<Vec<_>>();

    let mut gear_to_nums = HashMap::new();

    let mut s1 = 0;
    let mut num;
    for (y, line) in lines.iter().enumerate() {
        let re = Regex::new(r"\d+").unwrap();
        for cap in re.captures_iter(line).map(|g| g.get(0).unwrap()) {
            num = line[cap.start()..cap.end()].parse::<i32>().unwrap();
            let mut good = false;
            for ya in y as i32 - 1..y as i32 + 2 {
                for xa in cap.start() as i32 - 1..cap.end() as i32 + 1 {
                    if is_valid(ya, xa, &lines) {
                        let c = lines[ya as usize].chars().nth(xa as usize).unwrap();
                        good |= !c.is_ascii_digit() && c != '.';
                        if c == '*' {
                            gear_to_nums.entry((ya, xa)).or_insert_with(Vec::new).push(num);
                        }
                    }
                }
            }
            if good {
                s1 += num;
            }
        }
    }
    let s2: i32 = gear_to_nums
        .values()
        .filter(|v| v.len() == 2)
        .map(|v| v[0] * v[1])
        .sum();
    println!("{}\n{}", s1, s2);
}