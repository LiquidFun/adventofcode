use std::{collections::HashSet, io::stdin};

use regex::Regex;

fn adjacent((x, y): &(i32, i32)) -> impl Iterator<Item = (i32, i32)>  {
    [(x-2, *y), (x+2, *y), (x+1, y+1), (x+1, y-1), (x-1, y-1), (x-1, y+1)].into_iter()
}

fn main() {
    let pat = Regex::new("e|ne|nw|w|sw|se").unwrap();
    let mut tiles = HashSet::new();

    for line in stdin().lines().filter_map(Result::ok) {
        let (mut x, mut y) = (0, 0);
        for dir in pat.find_iter(&line).map(|m| m.as_str()) {
            x += (dir.contains('e') as i32 * 4 - 2) / dir.len() as i32;
            y += dir.contains('n') as i32 - dir.contains('s') as i32;
        }
        if !tiles.remove(&(x, y)) {
            tiles.insert((x, y));
        }
    }
    println!("{}", tiles.len());

    for _ in 0..100 {
        tiles = tiles.iter()
            .flat_map(adjacent)
            .filter(|t| (1 + !tiles.contains(t) as usize..=2)
                .contains(&adjacent(t).filter(|a| tiles.contains(a)).count()))
            .collect();
    }
    println!("{}", tiles.len());
}
