use std::io::{self, Write};
use std::process::Command;

fn ui() {
    loop {
        println!("1. DDoS");
        println!("2. Info");
        println!("3. Exit");

        print!("--> ");
        io::stdout().flush().unwrap();

        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        let input = input.trim();

        match input {
            "1" => {
                let output = Command::new("python")
                    .arg("modules.py")
                    .output()
                    .expect("Failed to run");

                if output.status.success() {
                    println!("Is working");
                    println!("{}", String::from_utf8_lossy(&output.stdout));
                } else {
                    eprintln!("Error: {}", String::from_utf8_lossy(&output.stderr));
                }
            }
            "2" => {
                println!("This is some information.");
            }
            "3" => {
                println!("Exiting...");
                break;
            }
            _ => {
                println!("Invalid option, please try again.");
            }
        }
    }
}

fn main() {
    ui();
}