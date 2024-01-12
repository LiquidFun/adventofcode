use std::io::stdin;

const DIRS: [(i32, i32); 4] = [(0, 1), (1, 0), (0, -1), (-1, 0)];

fn part1(actions: &Vec<(String, i32)>) -> i32 {
    let (mut y, mut x, mut dir) = (0, 0, 0);
    for (action, num) in actions {
        match action.as_str() {
            "N" => y -= num,
            "S" => y += num,
            "W" => x -= num,
            "E" => x += num,
            "F" => {y += DIRS[dir as usize].0 * num; x += DIRS[dir as usize].1 * num },
            "R" => dir = (dir + num / 90 + 4) % 4,
            "L" => dir = (dir - num / 90 + 4) % 4,
            _ => panic!(),
        }
    }
    y.abs() + x.abs()
}

fn part2(actions: &Vec<(String, i32)>) -> i32 {
    let (mut y, mut x) = (0, 0);
    let (mut wpy, mut wpx) = (-1, 10);
    for (action, num) in actions {
        match (action.as_str(), num) {
            ("N", _) => wpy -= num,
            ("S", _) => wpy += num,
            ("W", _) => wpx -= num,
            ("E", _) => wpx += num,
            ("F", _) => {y += wpy * num; x += wpx * num },
            ("R", 90) | ("L", 270) => {(wpy, wpx) = (wpx, -wpy)},
            ("R", 270) | ("L", 90) => {(wpy, wpx) = (-wpx, wpy)},
            ("R", 180) | ("L", 180) => {(wpy, wpx) = (-wpy, -wpx)},
            _ => panic!(),
        }
    }
    y.abs() + x.abs()
}

fn main() {
    let actions: Vec<(String, i32)> = stdin().lines()
        .filter_map(Result::ok)
        .map(|l| (l[0..1].to_owned(), l[1..l.len()].parse().unwrap()))
        .collect();
    println!("{}\n{}", part1(&actions), part2(&actions));
}