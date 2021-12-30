use std::io::BufRead;

fn intvec_from_file(path: &str) -> Vec<i64> {
  let f = std::fs::File::open(path).expect("Panic: input file not found!");
  let r = std::io::BufReader::new(f);
  let n: Vec<i64> = r
    .lines()
    .map(|l| l.unwrap().parse::<i64>().unwrap())
    .collect();
  return n;
}

fn main() {
  let v = intvec_from_file("input.txt");
  let answer : i64 = (1..v.len()).map(|p| if v[p-1] < v[p] {1} else {0}).sum();
  println!("{:?}", answer);
}