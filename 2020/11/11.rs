use std::{io::stdin, collections::HashSet};
use itertools::{iproduct, Itertools};

const DIRS: [(i32, i32); 8] = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)];

fn solve(lines: &Vec<Vec<char>>, is_part2: bool) {

    let seats: Vec<_> = iproduct!(0..lines.len(), 0..lines[0].len())
        .filter(|(y, x)| lines[*y][*x] == 'L')
        .map(|(y, x)| (y as i32, x as i32))
        .collect();

    // let is_seat = |y, x| seats.contains(x)

    let mut taken = HashSet::new();
    let s = lines.len() as i32;
    loop {
        let mut new_taken = HashSet::new();
        for seat in &seats {
            let mut adj = DIRS.iter()
                .filter(|&(y, x)| taken.contains(&(seat.0+y, seat.1+x)))
                .count();
            if is_part2 {
                adj = DIRS.iter()
                    .map(|&(y, x)| (y, x, (1..s).find(|m| seats.contains(&(seat.0+y*m, seat.1+x*m))).unwrap_or(1)))
                    .filter(|&(y, x, m)| taken.contains(&(seat.0+y*m, seat.1+x*m)))
                    .count();
            }
            match adj {
                0 => new_taken.insert(seat),
                4 if !is_part2 => false,
                5..=8 => false,
                _ if taken.contains(seat) => new_taken.insert(seat),
                _ => false,
            };
        }
        if taken.len() == new_taken.len() {
            break
        }
        taken = new_taken;
    }
    println!("{:?}", taken.len());
}

fn main() {
    let lines: Vec<Vec<_>> = stdin().lines()
        .map(|line| line.unwrap().trim().chars().collect_vec())
        .collect();
    solve(&lines, false);
    solve(&lines, true);
}