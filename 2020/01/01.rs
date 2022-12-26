use std::io::Read;

fn read_nums() -> Vec<i32> {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    input
        .lines()
        .map(|line| line.parse::<i32>().unwrap())
        .collect::<Vec<_>>()
}

fn main() {
    let nums = read_nums();
    let mut ans2 = 0;
    for i in 0..nums.len() {
        for j in i+1..nums.len() {
            for k in j+1..nums.len() {
                if nums[i] + nums[j] + nums[k] == 2020 {
                    ans2 = nums[i] * nums[j] * nums[k]
                }
            }
            if nums[i] + nums[j] == 2020 {
                println!("{}", nums[i] * nums[j])
            }
        }
    }
    println!("{}", ans2)
}