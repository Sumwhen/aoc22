pub mod gridposition {
    use std::collections::HashSet;

    pub fn part2(instructions: Vec<String>) -> u32 {
        // let instructions =
        let mut positions: Vec<Position2D> = Vec::new();
        let mut visited: HashSet<_> = HashSet::new();
        for i in 0..10 {
            positions.push(Position2D(0,0));
        }
        for instruction in instructions {

            let s = instruction.split(" ").collect::<Vec<&str>>();
            let dir = Position2D::parse(s[0]);
            let amount  =  s[1].parse::<u32>().unwrap();
            for _i in 0..amount {

                let n= &dir + &positions[0];
                positions[0] = n.clone();
                for i in 1..10 {

                    positions[i] = positions[i].follow(&positions[i - 1]);
                }
                let suc = visited.insert(positions[9]);

            }
        }
        visited.len() as u32
    }

    #[derive(Debug, Copy, Clone, Hash)]
    pub struct Position2D(i32, i32);


    #[derive(Debug)]
    struct Knot {
        pos: Position2D
    }


    impl Add<&Position2D> for &Position2D {
        type Output = Position2D;
        fn add(self, rhs: &Position2D) -> Self::Output {
            Position2D {
                0: self.0 + rhs.0,
                1: self.1 + rhs.1
            }
        }
    }
    impl AddAssign<Position2D> for Position2D {
        fn add_assign(&mut self, rhs: Position2D) {
            self.0 += rhs.0;
            self.1 += rhs.1;
        }
    }

    impl Add<i32> for Position2D {
        type Output = Self;
        fn add(self, rhs: i32) -> Self::Output {
            Position2D(self.0 + rhs, self.1 + rhs)
        }
    }

    impl Sub<i32> for Position2D {
        type Output = Self;
        fn sub(self, rhs: i32) -> Self::Output {
            Position2D(self.0 - rhs, self.1 - rhs)
        }
    }

    impl Sub<&Position2D> for Position2D {
        type Output = Self;
        fn sub(self, rhs: &Position2D) -> Self::Output {
            Position2D(self.0 - rhs.0, self.1 - rhs.1)
        }
    }
    impl Sub<&Position2D> for &Position2D {
        type Output = Position2D;
        fn sub(self, rhs: &Position2D) -> Self::Output {
            Position2D(self.0 - rhs.0, self.1 - rhs.1)
        }
    }

    impl Sub<Position2D> for &Position2D {
        type Output = Position2D;
        fn sub(self, rhs: Position2D) -> Self::Output {
            Position2D(self.0 - rhs.0, self.1 - rhs.1)
        }
    }


    trait Normalize<T> {
        type Output;
        fn norm(self) -> Self::Output;
    }

    impl Normalize<&Position2D> for &Position2D {

        type Output = Position2D;
        fn norm(self) -> Self::Output {
            Position2D(self.0.signum(), self.1.signum())
        }

    }

    impl PartialEq for Position2D {
        fn eq(&self, other: &Self) -> bool {
            self.0 == other.0 && self.1 == other.1
        }
    }

    impl Eq for Position2D {}


    impl Position2D {
        fn manhattan_distance(&self, pos: &Position2D) -> i32 {
            (pos.1 - self.1).abs() + (pos.0 - self.0).abs()
        }

        fn is_neighbor(&self, pos: &Position2D) -> bool {
            let diff = &(pos - self);
            let dn = diff.norm();
            dn == *diff
        }
        // follows the pos
        fn follow(self, pos: &Position2D) -> Position2D {

            let diff = pos - &self;
            let dir = diff.norm();
            if !self.is_neighbor(pos) {
                &self + &dir
            } else {
                self
            }
        }

        fn empty() -> Position2D {
            Position2D(0,0)
        }

        fn parse(s: &str) -> Position2D {
            match s {
                "R" => Position2D(1, 0),
                "L" => Position2D(-1, 0),
                "U" => Position2D(0, 1),
                "D" => Position2D(0, -1),
                _ => Position2D::empty()
            }
        }
    }

}