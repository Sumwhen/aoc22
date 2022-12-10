

pub fn solve_1(lines: Vec<String>) -> i32 {
    let mut cycle:u32  = 0;
    let mut register = 1;
    let mut total = 0;
    for l in lines {
        // println!("{}", l);
        let parts = l.split(" ").collect::<Vec<&str>>();
        let command = parts[0].clone();
        let arg;
        cycle += 1;
        print_sprite(cycle, register);
        match command {
            "addx" => {
                arg = parts[1].clone();
                // check for mod 40
                total += get_signal_strength(cycle, register);
                cycle += 1;
                print_sprite(cycle, register);
                total += get_signal_strength(cycle, register);
                let f = arg.parse::<i32>().unwrap();
                // println!("f: {}", f);
                register += f
                // check for mod 40
            }
            "noop" => {
                total += get_signal_strength(cycle, register);
            }
            _ => {}
        };

    }
    total
}
fn print_sprite(cycle: u32, register: i32) {
    let modd = (cycle - 1) % 40;

    if modd == 0 {
        println!("  {}", cycle)
    }
    if (-1..=1).filter(|l| (register + l) == modd as i32).collect::<Vec<i32>>().len() > 0 {
        print!("#");
    } else {
        print!(" ");
    }


}
fn get_signal_strength(cycle: u32, register: i32) -> i32 {
    if ((cycle as i32 - 20) % 40) == 0 {
        return register * cycle as i32;
    }
    0
}