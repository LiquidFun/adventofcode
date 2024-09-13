for dir in {0,1,2}*; do cargo build --release --bin $dir; done
for dir in {0,1,2}*; do hyperfine -N --min-runs 1 --warmup 3 --input $dir/input.in ./target/release/$dir; done
