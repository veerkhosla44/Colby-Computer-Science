// Differences from C:
// - Rust supports higher-order functions more naturally, allowing functions to be passed as arguments or assigned to variables with full type safety.
// - Rust's fn type is used for function pointers, enhancing type safety and clarity.

// Defines a function that takes an i32 and returns its value incremented by 1.
fn add_one(x: i32) -> i32 {
    x + 1
}

// Demonstrates using a function as a parameter to another function.
fn do_twice(f: fn(i32) -> i32, arg: i32) -> i32 {
    f(arg) + f(arg) // Calls the passed function twice with the provided argument.
}

fn main() {
    // Calls do_twice with add_one as the function parameter and 5 as the argument.
    let result = do_twice(add_one, 5);
    println!("The result is {}", result);

    // Assigns a function to a variable and then calls it.
    let f: fn(i32) -> i32 = add_one;
    let six = f(5);
    println!("The result is {}", six);
}