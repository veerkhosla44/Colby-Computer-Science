/* Veer Khosla
CS333
3/17/24
Performs binary search on an array of numbers
*/

// Struct representing a person
struct Person {
    name: String,
    age: u32,
    is_student: bool,
}

fn main() {
    // Basic built-in types
    let integer: i32 = 10;
    let float: f64 = 3.14;
    let character: char = 'A';
    let boolean: bool = true;

    // Aggregate type (struct)
    let person1 = Person {
        name: String::from("Alice"),
        age: 25,
        is_student: false,
    };

    let person2 = Person {
        name: String::from("Bob"),
        age: 30,
        is_student: true,
    };

    // Operations with built-in types
    let sum = integer + 5; // Result is an integer
    let product = float * 2.0; // Result is a float
    let modulo = integer % 3; // Result is an integer

    // Printing results
    println!("Sum: {}", sum);
    println!("Product: {}", product);
    println!("Modulo: {}", modulo);

    // Accessing struct fields
    println!("Name: {}", person1.name);
    println!("Age: {}", person1.age);
    println!("Is Student: {}", person1.is_student);

    println!("Name: {}", person2.name);
    println!("Age: {}", person2.age);
    println!("Is Student: {}", person2.is_student);
}
