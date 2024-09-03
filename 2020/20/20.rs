use std::{collections::{HashMap, HashSet}, io::stdin};

use itertools::Itertools;

fn main() {
    let input = stdin().lines().filter_map(Result::ok).join("\n").replace(".", "0").replace("#", "1");
    let blocks = input.split("\n\n").collect_vec();

    let mut tiles = HashMap::new();
    let mut edges: HashMap<i32, HashSet<i32>> = HashMap::new();

    for block in blocks {
        let num: i32 = block.lines().next().unwrap().trim_matches(['T', 'i', 'l', 'e', ' ', ':']).parse().unwrap();
        let tile = block.lines().skip(1).collect_vec();
        tiles.insert(num, tile.clone());


        for edge in vec![
            tile.first().unwrap().parse::<i32>().unwrap(),
            tile.first().unwrap().chars().rev().join("").parse::<i32>().unwrap(),
            tile.last().unwrap().parse::<i32>().unwrap(),
            tile.last().unwrap().chars().rev().join("").parse::<i32>().unwrap(),
            tile.iter().map(|l| l.chars().next().unwrap()).join("").parse::<i32>().unwrap(),
            tile.iter().map(|l| l.chars().last().unwrap()).join("").parse::<i32>().unwrap(),
            tile.iter().map(|l| l.chars().next().unwrap()).rev().join("").parse::<i32>().unwrap(),
            tile.iter().map(|l| l.chars().last().unwrap()).rev().join("").parse::<i32>().unwrap(),
        ] {
            edges.entry(edge).or_insert_with(HashSet::new).insert(num);
        }
        println!("{:?}", edges);
        println!("{:?}", edges.iter().filter(|(_, v)| v.len() == 1).map(|(_, v)| v.iter().next().unwrap()).sorted().collect_vec());
    }
}