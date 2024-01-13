use std::io::stdin;

fn mod_inv(a: i64, module: i64) -> i64 {
    let mut mn = (module, a);
    let mut xy = (0, 1);

    while mn.1 != 0 {
        xy = (xy.1, xy.0 - (mn.0 / mn.1) * xy.1);
        mn = (mn.1, mn.0 % mn.1);
    }
    while xy.0 < 0 {
        xy.0 += module;
    }
    xy.0
}

fn chinese_remainder_theorem(pairs: &Vec<(i64, i64)>) -> i64 {
    let prod: i64 = pairs.iter().map(|t| t.1).product();
    let mut sum = 0;
    for (s, x) in pairs {
        let p = prod / x;
        let residue = (x - s) % x;
        sum += residue * mod_inv(p, *x) * p;
    }
    sum % prod
}

fn main() {
    let lines = stdin().lines().filter_map(Result::ok).collect::<Vec<_>>();

    let time: i32 = lines.first().unwrap().parse().unwrap();
    lines[1].split(",")
        .filter_map(|s| s.parse().ok())
        .map(|t: i32| (t - time % t, t))
        .min()
        .map(|(b, t)| println!("{}", b*t));

    let pairs = lines[1].split(",")
        .enumerate()
        .filter_map(|(i, s)| s.parse().ok().map(|n| (i as i64, n)))
        .collect::<Vec<_>>();
    println!("{:?}", chinese_remainder_theorem(&pairs));
}