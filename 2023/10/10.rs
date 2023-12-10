use std::{io::{stdin, Read}, collections::{VecDeque, HashSet}};

use itertools::{Itertools, izip, iproduct};

const DIR: [(i32, i32); 4] = [(0, 1), (1, 0), (-1, 0), (0, -1)];
const ALLOW_TO: [&str; 4] = ["-7J", "|JL", "|F7", "-FL"];
const ALLOW_FROM: [&str; 4] = ["-FLS", "|F7S", "|JLS", "-7JS"];

fn in_bounds(y: i32, x: i32, ys: usize, xs: usize) -> Option<(usize, usize)> {
    match (usize::try_from(y), usize::try_from(x)) {
        (Ok(y2), Ok(x2)) if y2 < ys && x2 < xs => Some((y2, x2)),
        _ => None,
    }
}

fn main() {
    let mut input = String::new();
    stdin().read_to_string(&mut input).unwrap();
    let lines: Vec<&str> = input.lines().collect_vec();
    let (ys, xs) = (lines.len(), lines.get(0).unwrap().len());

    let start = input.lines()
        .find_position(|line| line.contains('S'))
        .map(|o| (o.0, o.1.find('S').unwrap(), 0));

    let mut q = VecDeque::from([start.unwrap()]);
    println!("{:?}", q);

    let mut visited = HashSet::new();
    let at = |y: usize, x: usize| lines[y].chars().nth(x).unwrap();
    let mut inside: HashSet<(usize, usize)> = iproduct!(0..ys, 0..xs).collect();

    let mut max_dist = 0;
    while !q.is_empty() {
        let (y, x, dist) = q.pop_front().unwrap();
        visited.insert((y+y+1, x+x+1));
        inside.remove(&(y, x));
        max_dist = max_dist.max(dist);
        for ((dy, dx), to, from) in izip!(DIR, ALLOW_TO, ALLOW_FROM) {
            if let Some((ya, xa)) = in_bounds(y as i32+dy, x as i32+dx, ys, xs) {
                if to.contains(at(ya, xa)) && from.contains(at(y, x)) {
                    if !visited.contains(&(y+ya+1, x+xa+1)) {
                        visited.insert((y+ya+1, x+xa+1));
                        q.push_back((ya, xa, dist+1));
                    }
                }
            }
        }
    }
    q.push_back((0, 0, 0));

    while !q.is_empty() {
        let (y, x, _) = q.pop_front().unwrap();
        visited.insert((y, x));
        if let Some((ydiv2, xdiv2)) = in_bounds((y as i32-1)/2, (x as i32-1)/2, ys, xs) {
            inside.remove(&(ydiv2, xdiv2));
        }
        for (dy, dx) in DIR {
            if let Some((ya, xa)) = in_bounds(y as i32+dy, x as i32+dx, ys*2+1, xs*2+1) {
                if !visited.contains(&(ya, xa)) {
                    visited.insert((ya, xa));
                    q.push_back((ya, xa, 0));
                }
            }
        }
    }

    println!("{}\n{}", max_dist, inside.len());
}