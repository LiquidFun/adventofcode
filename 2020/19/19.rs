use std::{collections::HashMap, io::stdin};

use itertools::Itertools;
use regex::Regex;

fn resolve(
    curr: &str,
    rules: &HashMap<String, Vec<Vec<String>>>,
    resolved: &mut HashMap<String, String>,
) -> String {
    if let Some(value) = resolved.get(curr) {
        return value.to_string();
    }
    let rule = rules.get(curr).unwrap();
    let pattern = rule
        .iter()
        .map(|v| v.iter().map(|s| resolve(s, rules, resolved)).join(""))
        .join("|");
    let pat = format!("({pattern})");
    resolved.insert(curr.to_owned(), pat.clone());

    return pat;
}

fn main() {
    let lines = stdin().lines().filter_map(Result::ok).join("\n");

    let (rules_str, messages) = lines.split("\n\n").next_tuple().unwrap();
    let mut rules = HashMap::new();
    for rule in rules_str.lines() {
        let (index, sub) = rule.split(":").next_tuple().unwrap();
        rules.insert(
            index.to_owned(),
            sub.split("|")
                .map(|nums| nums.trim().split(" ").map(|v| v.to_owned()).collect_vec())
                .collect_vec(),
        );
    }
    let mut resolved: HashMap<String, String> = rules
        .iter()
        .map(|(k, v)| (k, v.first().unwrap().first().unwrap()))
        .filter(|(_, s)| s.contains('"'))
        .map(|(&ref k, v)| (k.to_owned(), v.trim_matches('"').to_owned()))
        .collect();

    let p42 = resolve("42", &rules, &mut resolved);
    let p31 = resolve("31", &rules, &mut resolved);
    let regex1 = Regex::new(&format!("^{p42}{p42}{p31}$")).unwrap();
    println!("{}", messages.lines().filter(|l| regex1.is_match(l)).count());

    let pattern2 = (1..6).map(|i| format!("({p42}+{p42}{{{i}}}{p31}{{{i}}})")).join("|");
    let regex2 = Regex::new(&format!("^({pattern2})$")).unwrap();
    println!("{}", messages.lines().filter(|l| regex2.is_match(l)).count());
}