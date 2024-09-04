use std::{collections::{HashMap, HashSet}, io::stdin};

use itertools::Itertools;
use regex::Regex;

#[derive(Clone, Debug, PartialEq, Eq)]
struct Tile {
    id: usize,
    rows: Vec<usize>,
}



impl Tile {
    fn new(id: usize, lines: Vec<&str>) -> Tile {
        Tile { id: id, rows: lines.iter().map(|s| usize::from_str_radix(s, 2).unwrap()).collect_vec() }
    }

    fn flipped(&self) -> Tile {
        let a = self.rows.iter().map(|i| format!("{i:010b}").chars().rev().join("")).collect_vec();
        Tile::new(self.id, a.iter().map(|i| i.as_str()).collect_vec())
    }

    fn rotated(&self) -> Tile {
        Tile {
            id: self.id,
            rows: (0..10).map(|i| (0..10).map(|j| (self.rows.get(9-j).unwrap() & (1<<i)) / (1<<i) * (1<<j)).sum()).collect()
        }
    }
    
    fn inner(&self) -> Tile {
        Tile {
            id: self.id,
            rows: self.rows.iter().skip(1).take(8).map(|n| (n - (n & (1<<9))) >> 1).collect()
        }
    }

    fn top(&self) -> usize { *self.rows.first().unwrap() }
    fn bot(&self) -> usize { *self.rows.last().unwrap() }
    fn left(&self) -> usize { self.rotated().bot() }
    fn right(&self) -> usize { self.rotated().top() }
    
    fn variations(&self) -> Vec<Tile> {
        let mut tiles = Vec::new();
        let mut tile = self.clone();
        (0..4).for_each(|_| { tile = tile.rotated(); tiles.push(tile.clone()); tiles.push(tile.flipped()) });
        tiles
        // vec![
        //     self.clone(),
        //     self.rotated(),
        //     self.rotated().rotated(),
        //     self.rotated().rotated().rotated(),
        //     self.flipped(),
        //     self.rotated().flipped(),
        //     self.rotated().rotated().flipped(),
        //     self.rotated().rotated().rotated().flipped(),
        // ]
    }

    fn left_edges(&self) -> HashMap<usize, Tile> {
        self.variations().iter().map(|tile| (tile.left(), tile.clone())).collect()
    }

    fn top_edges(&self) -> HashMap<usize, Tile> {
        self.variations().iter().map(|tile| (tile.top(), tile.clone())).collect()
    }
}


fn solve(corner: &Tile, all_tiles: &Vec<Tile>) -> usize {
    let size = (0..).find(|i| i*i == all_tiles.len() / 8).unwrap();

    let mut leftmost = corner.clone();
    let mut used = HashSet::new();

    let mut field: Vec<Vec<char>> = Vec::new();

    for y in 0..size {
        let mut current = leftmost.clone();
        if y != 0 {
            current = all_tiles.iter().filter(|t| !used.contains(&t.id)).find(|tile| tile.top() == leftmost.bot()).unwrap().clone();
        }
        leftmost = current.clone();
        used.insert(current.id);
        current.inner().rows.iter().for_each(|n| field.push(format!("{n:08b}").chars().collect()));
        for _ in 1..size {
            // println!("{:?}", current.right());
            current = all_tiles.iter().filter(|t| !used.contains(&t.id)).find(|tile| tile.left() == current.right()).unwrap().clone();
            // println!("{:?}", current.left());
            used.insert(current.id);

            for (row, num) in current.inner().rows.iter().enumerate() {
                field.get_mut(y*8+row).unwrap().extend(format!("{num:08b}").chars());
            }
        }
        // field.push("-".repeat(field.get(0).unwrap().len()).chars().collect_vec())
    }
    let lines = field.iter().map(|vec| vec.iter().join("")).collect_vec();
    // lines.iter().map(|v| v.iter().join("")).for_each(|l| println!("{:?}", l));
                        // "                  # "
                        // "#    ##    ##    ###"
                        // " #  #  #  #  #  #   "
    let dragon1 = Regex::new(r"..................1.").unwrap();
    let dragon2 = Regex::new(r"1....11....11....111").unwrap();
    let dragon3 = Regex::new(r".1..1..1..1..1..1...").unwrap();
    // lines.windows(3).for_each(|w| println!("{:?}", w));
    let mut dragons = 0;
    for (a, b, c) in lines.iter().tuple_windows() {
        for i in 0..a.len() {
            println!("match {:?}", &a.chars().skip(i).take(20).join(""));
            if dragon1.is_match(&a.chars().skip(i).take(20).join(""))
                && dragon2.is_match(&b.chars().skip(i).take(20).join(""))
                && dragon3.is_match(&c.chars().skip(i).take(20).join("")) {
                dragons += 15;
                // println!("match {:?}", &b.iter().skip(i).take(20).join(""));
                // println!("match {:?}", &c.iter().skip(i).take(20).join(""));
            }
        }
    }
    // let wins = lines.iter().map(|l| l.chars().collect_vec().windows(20).map(|w| w.iter().join("")).collect_vec()).collect_vec();
    // for (a, b, c) in wins.iter().tuple_windows() {
    //     println!("{:?}", a);
    // }
    lines.join("").matches("1").count() - dragons
}

fn main() {
    let input = stdin().lines().filter_map(Result::ok).join("\n").replace(".", "0").replace("#", "1");
    let blocks = input.split("\n\n").collect_vec();

    // let mut tiles = HashMap::new();
    let mut tiles = Vec::new();
    let mut edges: HashMap<usize, HashSet<usize>> = HashMap::new();

    for block in blocks {
        let num: usize = block.lines().next().unwrap().trim_matches(['T', 'i', 'l', 'e', ' ', ':']).parse().unwrap();
        let tile = Tile::new(num, block.lines().skip(1).collect());
        // tiles.insert(num, tile.clone());
        block.lines().for_each(|line| println!("{}", line));
        tiles.push(tile.clone());
        assert!(tile == tile.flipped().flipped());
        assert!(tile != tile.flipped());
        assert!(tile == tile.rotated().rotated().rotated().rotated());
        assert!(tile.left() == tile.flipped().flipped().left());
        assert!(tile.left() == tile.rotated().rotated().rotated().rotated().left());
        assert!(tile.rotated().left() == tile.rotated().left());
        assert!(tile.flipped().flipped().top() == tile.rotated().rotated().rotated().rotated().top());
        assert!(tile.variations().len() == 8);
        assert!(tile != tile.rotated().rotated(), "{:?}", block);
        // println!("\ntop {:010b}", tile.top());
        // println!("left {:010b}", tile.left());
        // println!("right {:010b}", tile.right());
        // assert!(tile.top() == tile.rotated().left());

        println!("{:?}", tile.variations().len());

        println!("{:?}", tile.variations());

        for (edge, _) in tile.top_edges() {
            println!("edge {:?}", edge);
            edges.entry(edge).or_insert_with(HashSet::new).insert(num);
        }
    }
    println!("{:?}", edges);

    // tiles.iter()
    //     .flat_map(|tile| tile.variations())
    //     .filter(|tile| !edges.contains_key(&tile.left()))
    //     .for_each(|tile| println!("{:?}", tile.left()));

    println!("{:?}", "hello");

    let all_tiles = tiles.iter().flat_map(|tile| tile.variations()).collect_vec();

    let corners = all_tiles.iter()
        .filter(|t| edges.get(&t.top()).unwrap().len() == 1)
        .filter(|t| edges.get(&t.left()).unwrap().len() == 1)
        .collect_vec();

    println!("{:?}", corners.iter().map(|tile| tile.id).unique().reduce(|acc, a| acc * a).unwrap());

    println!("{:?}", corners.iter().map(|corner| solve(corner, &all_tiles)).collect_vec());
    // println!("{:?}", corners.iter().map(|corner| solve(corner, &all_tiles)).sum::<usize>());
    // 2129 too high
    // 2005 too low
    // 1900 too low
    // println!("{:?}", edges.iter().filter(|(_, v)| v.len() == 1).map(|(_, v)| v.iter().next().unwrap()).sorted().collect_vec());
}