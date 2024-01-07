use std::{io::stdin, collections::HashMap};
use regex::Regex;

fn contains_shiny_gold(map: &HashMap<&str, Vec<[&str; 2]>>, key: &str) -> bool {
    if key == "shiny gold" { return true }
    map[key].iter().any(|[_, name]| contains_shiny_gold(map, name))
}

fn count_bags(map: &HashMap<&str, Vec<[&str; 2]>>, key: &str) -> usize {
    map[key].iter()
        .map(|[num, name]| num.parse::<usize>().unwrap()*count_bags(map, name))
        .sum::<usize>() + 1
}

fn main() {
    let pat = Regex::new(r"(^|\d) ?(\w+ \w+)").unwrap();
    let lines = stdin().lines().filter_map(Result::ok).collect::<Vec<_>>();
    let map = lines.iter()
        .map(|s| pat.captures_iter(&s).map(|c| c.extract::<2>()).collect::<Vec<_>>())
        .map(|m| (m[0].0, m.iter().skip(1).map(|s| s.1).collect::<Vec<_>>()))
        .collect::<HashMap<_, _>>();

    let p1 = map.iter().filter(|(key, _)| contains_shiny_gold(&map, key)).count();
    let p2: usize = count_bags(&map, "shiny gold");
    println!("{}\n{}", p1-1, p2-1);
}