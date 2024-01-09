use std::io::stdin;

fn main() {
    let nums: Vec<i64> = stdin().lines().map(|line| line.unwrap().parse().unwrap()).collect();
    let target_num = nums
        .windows(26)
        .find(|vec| !vec.iter().take(25).any(|n| vec.contains(&(vec[25]-n))))
        .unwrap()[25];

    let mut max = (0, 0);
    for i in 0..nums.len() {
        let mut sum = 0;
        for j in i..nums.len() {
            sum += nums[j];
            if sum == target_num && j-i > max.0 {
                max = (j-i, nums[i..=j].iter().min().unwrap() + nums[i..=j].iter().max().unwrap());
            }
        }
    }
    println!("{}\n{}", target_num, max.1);
}