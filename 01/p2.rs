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
  let read = intvec_from_file("input.txt");
  let v: Vec<i64> = (0..read.len()-2).map(|p| read[p]+read[p+1]+read[p+2]).collect();
  let answer : i64 = (1..v.len()).map(|p| if v[p-1] < v[p] {1} else {0}).sum();
  println!("{:?}", answer);
}