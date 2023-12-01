use std::io::Read;

// fn read_nums() -> Vec<i32> {
//     let mut input = String::new();
//     std::io::stdin().read_to_string(&mut input).unwrap();
//     input
//         .lines()
//         .map(|line| line.parse::<i32>().unwrap())
//         .collect::<Vec<_>>()
// }

fn main() {
    let digits1: Vec<_> = "0 1 2 3 4 5 6 7 8 9".split(" ").collect();
    let digits2: Vec<_> = "zero one two three four five six seven eight nine".split(" ").collect();
    // println!("{:?}", digits2);
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();

    let mut s1 = 0;
    let mut s2 = 0;
    for line in input.lines() {
        let mut nums: Vec<(usize, i32)> = vec![];
        digits1.iter()
            .for_each(|digit| line.match_indices(digit)
                .for_each(|i| nums.push((i.0, i.1.parse().unwrap())))
            
            );
        nums.sort();
        if nums.len() >= 1usize {
            s1 += nums.get(0).unwrap().1 * 10 + nums.last().unwrap().1;
        }

        digits2.iter()
            .for_each(|digit| line.match_indices(digit)
                .for_each(|i| nums.push((i.0, digits2.iter().position(|&x| x == i.1).unwrap() as i32)))
            );
        nums.sort();
        if nums.len() >= 1usize {
            s2 += nums.get(0).unwrap().1 * 10 + nums.last().unwrap().1;
        }

    }
    println!("{}\n{}", s1, s2);



}
