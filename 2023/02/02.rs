use std::io::Read;
use regex::Regex;
use std::cmp::max;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let re = Regex::new(r"(\d+) (r|g|b)").unwrap();

    let mut s1 = 0;
    let mut s2 = 0;
    for (index, line) in input.lines().enumerate() {
        let mut r = 0;
        let mut g = 0;
        let mut b = 0;
        for cap in re.captures_iter(line) {
            let num = cap.get(1).unwrap().as_str().parse().unwrap();
            let col = cap.get(2).unwrap().as_str();
            match col {
                "r" => r = max(r, num),
                "g" => g = max(g, num),
                "b" => b = max(b, num),
                _ => {}
            }

        }
        if r <= 12 && g <= 13 && b <= 14 {
            s1 += index + 1
        }
        s2 += r * g * b
    }
    println!("{}\n{}", s1, s2);
}
