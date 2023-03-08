use rand::Rng;
use std::cmp::Ordering;
use std::io;

fn main() {
    let secret_number: i8 = rand::thread_rng().gen_range(1..=100);
    // println!("{secret_number}");
    let mut score: i8 = 100;
    println!("Ready to play? Guess the number.");
    while score > 0 {
        println!("{score}");
        let mut guess = String::new();
        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line.");

        let guess: i8 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Please enter a number!");
                continue;
            }
        };

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("To low."),
            Ordering::Greater => println!("To high."),
            Ordering::Equal => {
                println!("Correct!");
                println!("Score: {}", score);
                break;
            }
        }
        score -= 1;
    }
    if score == 0 {
        println!("You lost! ");
    }
}
