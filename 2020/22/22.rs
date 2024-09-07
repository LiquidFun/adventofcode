use std::{collections::{HashSet, VecDeque}, io::stdin};

fn solve(mut player1: VecDeque<usize>, mut player2: VecDeque<usize>, part2: bool) -> bool {
    let is_first = player1.len() == player2.len();
    let mut cache = HashSet::new();
    while !player1.is_empty() && !player2.is_empty() {
        if !cache.insert((player1.clone(), player2.clone())) { return true; }
        let p1 = player1.pop_front().unwrap();
        let p2 = player2.pop_front().unwrap();
        let mut p1wins = p1 > p2;
        if part2 && player1.len() >= p1 && player2.len() >= p2 {
            p1wins = solve(player1.iter().take(p1).copied().collect(), player2.iter().take(p2).copied().collect(), true)
        }
        if p1wins {
            player1.extend([p1, p2])
        } else {
            player2.extend([p2, p1])
        }
    }
    if is_first {
        println!("{:?}", player1.iter().chain(player2.iter()).rev().zip(1..).fold(0, |acc, (i, v)| acc+i*v));
    }
    player2.is_empty()
}

fn main() {
    let mut player1: VecDeque<usize> = stdin().lines().map(|l| l.unwrap().parse()).filter_map(Result::ok).collect();
    let player2 = player1.split_off(player1.len() / 2);
    solve(player1.clone(), player2.clone(), false);
    solve(player1, player2, true);
}