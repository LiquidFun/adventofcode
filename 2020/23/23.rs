use std::{collections::VecDeque, io::stdin};

use itertools::Itertools;

fn solve(mut cups: VecDeque<u32>, steps: i32) -> VecDeque<u32> {
    let max = *cups.iter().max().unwrap();
    for i in 0..steps {
        // println!("{:?}", cups);
        if i % 1000 == 0 { println!("{:?}", i); }

        let curr = *cups.front().unwrap();
        cups.rotate_left(1);

        let mut dest = curr + max - 1;
        let three = cups.drain(..3).rev().collect_vec();
        while three.contains(&((dest - 1) % max + 1)) { dest -= 1; }
        let dest = (dest - 1) % max + 1;


        let pos = cups.iter().rev().position(|n| *n == dest).unwrap();
        three.iter().for_each(|v| cups.insert(pos+1, *v));
    }
    cups.rotate_left(cups.iter().position(|n| *n == 1).unwrap());
    cups
    // cups.iter().copied().cycle().skip_while(|n| *n != 1).take(cups.len()).collect()
}

fn main() {
    let cups: VecDeque<_> = stdin().lines().next().unwrap().unwrap().chars().map(|c| c.to_digit(10).unwrap()).collect();
    // println!("{:?}", cups);
    println!("{:?}", solve(cups.clone(), 100));
    let a: VecDeque<u32> = cups.into_iter().chain(10u32..1_000_000).collect();
    // for _ in 0..1_000_000 {
    //     // a.push_front(100);
    //     a.insert(500000, 100);
    // }
    // println!("{:?}", a);
    println!("{:?}", solve(a, 10_000_000).iter().take(10));
    // for _ in 0usize..100 {
    //     // let m = i % 9;
    //     let curr = cups.chars().next().unwrap().to_digit(10).unwrap() as i32;
    //     let mut dest = curr + 9 - 1;
    //     let mut to;
    //     loop {
    //         to = cups.find(&((dest - 1) % 9 + 1).to_string()).unwrap();
    //         if to > 3 { break; }
    //         dest -= 1;
    //     }
    //     // (1usize..=3).for_each(|j| cups.insert(to+j, cups.remove(j)));
    //     (1usize..=3).for_each(|j| cups.insert(to+j, cups.chars().nth(j).unwrap()));
    //     (1usize..=3).for_each(|j| { cups.remove(1); });
    //     let first = cups.remove(0);
    //     cups.push(first);
    //     println!("{:?}", cups);
    // }

    // println!("{:?}", cups.chars().cycle().skip_while(|c| *c != '1').skip(1).take(8).join(""));

}