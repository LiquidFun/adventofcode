use std::io::stdin;

use itertools::Itertools;

fn main() {
    let mut cups = stdin().lines().next().unwrap().unwrap();
    println!("{:?}", cups);
    for _ in 0usize..100 {
        // let m = i % 9;
        let curr = cups.chars().next().unwrap().to_digit(10).unwrap() as i32;
        let mut dest = curr + 9 - 1;
        eprintln!("curr = {:?}", curr);
        let mut to;
        loop {
            eprintln!("dest = {:?}", dest);
            to = cups.find(&((dest - 1) % 9 + 1).to_string()).unwrap();
            if to > 3 { break; }
            dest -= 1;
        }
        // (1usize..=3).for_each(|j| cups.insert(to+j, cups.remove(j)));
        (1usize..=3).for_each(|j| cups.insert(to+j, cups.chars().nth(j).unwrap()));
        (1usize..=3).for_each(|j| { cups.remove(1); });
        let first = cups.remove(0);
        cups.push(first);
        println!("{:?}", cups);
    }

    println!("{:?}", cups.chars().cycle().skip_while(|c| *c != '1').skip(1).take(8).join(""));

}