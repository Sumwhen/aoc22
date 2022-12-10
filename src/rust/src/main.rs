extern crate core;

use std::collections::{HashMap, HashSet};
use std::io::prelude::*;
use std::io::BufReader;
use std::fs::File;
use ndarray::prelude::*;
mod days;

const DAY: u32 = 10;
const TEST: bool = false;
const FILENAME_ADDITION: &str = "";
fn main() {
    // println!("part 1: {}", aoc9part1());

    // println!("part 2: {}", part2(read_lines("inputs/input9.txt")))
    println!("       ======= DAY {} =======\n", DAY);
    let mut k = String::with_capacity(30);
    if TEST {
        k.push_str("tests/test");
    } else {
        k.push_str("inputs/input");
    }
    k.push_str(FILENAME_ADDITION);
    k.push('.');
    k.push_str(&format!("{}", DAY));
    println!("path is {}", k);
    let input = read_lines(&k);
    println!("day 10 pt 1: {}", days::day10::solve_1(input));

}

fn read_lines(path: &str) -> Vec<String> {
    // first, reader
    let f = File::open(path).unwrap_or_else(|_| panic!("file not found:{}", path));
    let br = BufReader::new(f);
    br.lines()
        .map(|l| l.expect("parsing line failed"))
        .collect()
}


///
///
///
///
///     PT ONE STUFF
///
///
///
///
///
///





fn get_vector_for_dir(dir: &str) -> Option<Array1<i32>> {
    let mut directions = HashMap::from(
        [
            ("R", arr1(&[ 1,  0])),
            ("L", arr1(&[-1,  0])),
            ("U", arr1(&[ 0,  1])),
            ("D", arr1(&[ 0, -1])),
        ]
    );
    directions.remove(dir)
}

fn aoc9part1() -> usize {
    let instructions = read_lines("inputs/input9.txt");
    let mut head = arr1(&[0, 0]); // head starts at point zero
    let mut head_prev;
    let mut tail = arr1(&[0, 0]); // tail is underneath
    let mut positions = HashSet::new();
    positions.insert(arr1(&[0, 0]));
    for s in instructions {
        let inst = s.split(" ").collect::<Vec<_>>();
        let dirs = inst[0];
        let amount = inst[1].parse::<u32>().unwrap();
        let dir = get_vector_for_dir(dirs).unwrap();
        let mut diff;
        for _ in 0..amount {
            head_prev = head;
            head = &head_prev + &dir;
            diff = &head - &tail;
            if std::cmp::max(diff[0].abs(), diff[1].abs()) == 2 {
                let set = head_prev.clone();
                positions.insert(set);
                tail = head_prev;
            }
        }
    }

    positions.len()
}






fn aoc9part2() -> usize {
    let instructions = read_lines("input/input9.txt");
    let mut hm = HashSet::new(); // for storing the new positions of the tail
    hm.insert(arr1(&[0, 0])); // tail starts at 1
    // the head (which is moving every tick)
    let mut head = arr1(&[0, 0]);
    // the followers (who follow according to the rules)
    let mut followers = vec![arr1(&[0, 0]); 9];
    // the predecessors (similar to head_pred in function above, but generalized for all tail members)
    let mut preds = vec![arr1(&[0, 0]); 9];
    for instruction in instructions {
        let inst_pair = instruction.split(" ").collect::<Vec<_>>();
        let dir = get_vector_for_dir(inst_pair[0]).unwrap();
        let amount = inst_pair[1].parse::<usize>().unwrap();

        for _ in 0..amount {
            // first, move the head in the right direction
            head = &head + &dir;
            let curr = &head;
            // for each following knot, first look at the knot before (for the 0th knot this is head)
            for i in 0..9 {

            }
        }
    }
    for f in 0..9 {
        println!("{:?}", f);
    }



    hm.len()
}
