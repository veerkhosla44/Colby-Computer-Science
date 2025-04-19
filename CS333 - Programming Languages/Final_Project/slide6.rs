fn main() {
    let s1 = String::from("Hello, Rust!");
    borrow_string(&s1);
    println!("Still usable: {}", s1);  // Still valid here
}

fn borrow_string(data: &String) {
    println!("Borrowed data: {}", data);  // Prints "Hello, Rust!"
}
