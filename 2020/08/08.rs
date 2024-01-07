use std::{io::stdin, collections::HashSet};

fn terminates(inst: &Vec<(&str, i32)>) -> Result<i32, i32> {
    let mut visited = HashSet::new();
    let mut i: i32 = 0;
    let mut acc = 0;
    loop {
        let (op, num) = inst[i as usize];
        match op {
            "acc" => { acc += num; i += 1 },
            "nop" => i += 1,
            "jmp" => i += num,
            _ => panic!(),
        }
        if visited.contains(&i) {
            return Err(acc);
        }
        if !(0..inst.len() as i32).contains(&i) {
            return Ok(acc);
        }
        visited.insert(i);
    }
}

fn swap(op: &str) -> &str {
    match op {
        "nop" => "jmp",
        "jmp" => "nop",
        o => o,
    }
}

fn main() {
    let lines = stdin().lines().filter_map(Result::ok).collect::<Vec<_>>();
    let mut inst = lines.iter()
        .map(|line| line.split_once(" ").unwrap())
        .map(|(op, num)| (op, num.parse::<i32>().unwrap()))
        .collect::<Vec<_>>();
    println!("{:?}", terminates(&inst).unwrap_err());
    for i in 0..inst.len() {
        inst[i].0 = swap(inst[i].0);
        if let Ok(res) = terminates(&inst) {
            println!("{:?}", res);
        }
        inst[i].0 = swap(inst[i].0);
    }
}