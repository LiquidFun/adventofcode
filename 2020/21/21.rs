use std::{collections::{HashMap, HashSet}, io::stdin};
use itertools::Itertools;

fn main() {
    let lines = stdin().lines().filter_map(Result::ok).collect_vec();

    let mut all: Vec<&str> = Vec::new();
    let mut possible = HashMap::new();

    for line in &lines {
        let (left, right) = line.split_once(" (contains ").unwrap();
        let ingredients: HashSet<&str> = left.split(" ").collect();
        let allergens = right.trim_matches(')').split(", ").collect_vec();
        all.extend(&ingredients);

        for allergen in allergens {
            possible.entry(allergen)
                .or_insert(ingredients.clone())
                .retain(|k| ingredients.contains(k))
        }
    }
    println!("{}", all.iter().filter(|k| !possible.values().flatten().contains(k)).count());

    let mut pairings: HashMap<&str, &str> = HashMap::new();
    while possible.len() != pairings.len() {
        possible.iter()
            .filter(|(_, v)| v.len() == 1)
            .for_each(|(k, v)| { pairings.insert(k, v.iter().next().unwrap()); });
        possible.values_mut()
            .for_each(|v| v.retain(|a| !pairings.values().contains(a)))
    }
    println!("{}", pairings.iter().sorted().map(|(_, b)| b).join(","));
}