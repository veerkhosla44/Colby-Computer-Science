// Differences from C:
// - Rust's for loop iterates directly over items in a collection, unlike C's index-based iteration.
// - Rust's match is like C's switch but more versatile, allowing for pattern matching.
// - Rust's loop offers a cleaner way to write infinite loops compared to C's while(1).



fn main() {
    // Define an array of integers.
    let numbers = [10, 20, 30, 40, 50];
    // Initialize a mutable count variable.
    let mut count = 20;

    // if/else statement to check if count is less than 10.
    if count < 10 {
        println!("count is less than 10");
    } else {
        println!("count is at least 10");
    }

    // Infinite loop that decrements count until it reaches 0.
    loop {
        if count == 0 {
            println!("We've counted down to 0!");
            break; // Exit the loop when count is 0.
        }
        count -= 1; // Decrement count by 1.
    }

    // While loop that increments count until it reaches 5.
    while count < 5 {
        println!("count is: {}", count);
        count += 1; // Increment count by 1.
    }

    // For loop that iterates over each number in the numbers array.
    for number in numbers.iter() {
        println!("the number is: {}", number);
    }

    // Match statement, Rust's version of switch, used here to check if count is exactly 5.
    match count {
        5 => println!("Count is exactly 5"),
        _ => println!("Count is not 5"), // The '_' acts as a catch-all pattern.
    }
}
