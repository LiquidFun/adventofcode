use std::io::stdin;

fn eval(line: &str) -> i64 {
    let mut stack = vec![0, -1];
    eprintln!("line = {:?}", line);
    for c in line.chars() {
        let mut eval = false;
        eprintln!("c = {:?}, stack = {:?}", c, stack);
        match c {
            '0'..='9' => {
                stack.push(c.to_digit(10).unwrap() as i64);
                eval = true;
            }
            '(' => {
                stack.push(0);
                stack.push(-1);
            }
            ')' => {
                eval = true;
            },
            '+' => stack.push(-1),
            '*' => stack.push(-2),
            _ => (),
        }
        if eval {
            let digit1 = stack.pop().unwrap();
            let op = stack.pop().unwrap();
            let digit2 = stack.pop().unwrap();
            match op {
                -1 => stack.push(digit2 + digit1),
                _ => stack.push(digit2 * digit1),
            }
        }
    }
    *stack.get(0).unwrap()
}

fn main() {
    let out = stdin()
        .lines()
        .filter_map(Result::ok)
        .map(|line| eval(&line))
        .sum::<i64>();
    println!("{:?}", out)
}
