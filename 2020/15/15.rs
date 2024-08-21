use std::{io::stdin, collections::HashMap};

fn main() {
    let line = stdin().lines().last().unwrap().unwrap();
    let mut lookup: HashMap<_, _> = line.split(",").map(|n| n.parse().unwrap()).zip(1..).collect();
    let mut last = 0;
    for i in lookup.len()+1..30000000 {
        last = i - lookup.insert(last, i).unwrap_or(i);
        if i == 2019 { println!("{}", last); }
    }
    println!("{}", last);
}
