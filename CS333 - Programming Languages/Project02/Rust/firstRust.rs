// This Rust program calculates the factorial of a number.
use std::io;

fn main() {
    println!("Hello World!");
    println!("Enter a number to calculate its factorial:");
    
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    
    let n: u64 = input.trim().parse().expect("Please enter a valid number");
    let result = factorial(n);
    
    println!("Factorial of {} is: {}", n, result);
}

fn factorial(n: u64) -> u64 {
    if n == 0 {
        return 1;
    }
    n * factorial(n - 1)
}
