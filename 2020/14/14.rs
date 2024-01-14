use std::{collections::HashMap, io::stdin};

use itertools::Itertools;

fn mask_value(mask: &str, value: &str) -> i64 {
    let bin = format!("{:036b}", value.parse::<i64>().unwrap());
    let masked = mask
        .chars()
        .zip(bin.chars())
        .map(|(m, b)| if m == 'X' { b } else { m })
        .join("");
    i64::from_str_radix(&masked, 2).unwrap()
}

fn mask_address(mask: &str, addr: &str) -> Vec<i64> {
    let bin = format!("{:036b}", addr.parse::<i64>().unwrap());
    let x_ids: Vec<i64> = mask
        .char_indices()
        .filter(|t| t.1 == 'X')
        .map(|t| 1 << (35-t.0))
        .collect();

    let masked = mask
        .chars()
        .zip(bin.chars())
        .map(|(m, b)| match m { '0' => b, '1' => '1', _ => '0' })
        .join("");
    let num = i64::from_str_radix(&masked, 2).unwrap();

    (0..=x_ids.len())
        .flat_map(|k| {
            x_ids
                .iter()
                .combinations(k)
                .map(|comb| num + comb.iter().fold(0, |a, &b| a + b))
        })
        .collect()
}

fn main() {
    let lines: Vec<_> = stdin().lines().filter_map(Result::ok).collect();
    let mut memory1 = HashMap::new();
    let mut memory2 = HashMap::new();
    let mut mask = "";
    for line in &lines {
        if line.starts_with("mask") {
            mask = &line[7..line.len()];
        } else {
            let (addr, val) = line
                .strip_prefix("mem[")
                .unwrap()
                .split_once("] = ")
                .unwrap();
            memory1.insert(addr, mask_value(mask, val));
            for address in mask_address(mask, addr) {
                memory2.insert(address, val.parse().unwrap());
            }
        }
    }
    println!("{:?}", memory1.values().sum::<i64>());
    println!("{:?}", memory2.values().sum::<i64>());
}
