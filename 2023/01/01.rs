use std::io::Read;

const DIGITS: [&str; 10] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
const WORDS: [&str; 10] = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();

    let mut s1 = 0;
    let mut s2 = 0;
    for line in input.lines() {
        let mut nums: Vec<(usize, i32)> = vec![];
        DIGITS.iter().for_each(|digit| {
            line.match_indices(digit)
                .for_each(|i| nums.push((i.0, i.1.parse().unwrap())))
        });
        nums.sort();
        s1 += nums.first().unwrap_or(&(0, 0)).1 * 10 + nums.last().unwrap_or(&(0, 0)).1;

        WORDS.iter().for_each(|digit| {
            line.match_indices(digit).for_each(|i| {
                nums.push((i.0, WORDS.iter().position(|&x| x == i.1).unwrap() as i32))
            })
        });
        nums.sort();
        s2 += nums.first().unwrap_or(&(0, 0)).1 * 10 + nums.last().unwrap_or(&(0, 0)).1;
    }
    println!("{}\n{}", s1, s2);
}