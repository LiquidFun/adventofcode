use std::io::stdin;

fn solve(map: &Vec<String>, dy: usize, dx: usize) -> usize {
    let mut x = 0;
    let mut count = 0;
    for y in (0..map.len()).step_by(dy) {
        count += (map[y].get(x..=x).unwrap() == "#") as usize;
        x = (x+dx) % map[0].len();
    }
    count
}

fn main() {
    let map = stdin().lines().filter_map(Result::ok).collect();    
    println!("{}", solve(&map, 1, 3));
    let ans2: usize = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)].iter()
        .map(|(y, x)| solve(&map, *y, *x))
        .product();
    println!("{}", ans2);
}