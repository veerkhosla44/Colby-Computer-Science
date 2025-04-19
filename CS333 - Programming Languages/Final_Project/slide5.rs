fn main() {
    let s = String::from("Hello, Rust!");
    takes_ownership(s);
    // println!("{s}", s);  // Compile-time error: `s` value borrowed here after move
}

fn takes_ownership(data: String) {
    println!("Data: {}", data);  // Successfully prints "Hello, Rust!"
}