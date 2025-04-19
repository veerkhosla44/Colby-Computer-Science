/* Veer Khosla
CS333
3/17/24
Describes and demonstrates rules for variable declarations and identifier naming and scoping  
*/


fn main() {
    // Variable naming and declaration
    let my_variable: i32 = 10; // Declares a variable named 'my_variable' of type i32 with an initial value of 10
    let mut mutable_variable = 20; // Declares a mutable variable named 'mutable_variable' with an initial value of 20
    let _underscore_variable = 30; // Declares a variable named '_underscore_variable' with an initial value of 30

    // Accessing and printing variables
    println!("Value of my_variable: {}", my_variable); // Prints the value of 'my_variable'
    println!("Value of mutable_variable: {}", mutable_variable); // Prints the value of 'mutable_variable'
    
    // Modifying mutable variable
    mutable_variable = 25; // Modifies the value of 'mutable_variable'
    println!("Modified value of mutable_variable: {}", mutable_variable); // Prints the modified value of 'mutable_variable'

    // Variable scoping
    {
        let scoped_variable = 40; // Declares a variable with limited scope
        println!("Value of scoped_variable: {}", scoped_variable); // Prints the value of 'scoped_variable'
    } // 'scoped_variable' goes out of scope here

    // Attempting to access 'scoped_variable' here would result in a compile-time error

    // Shadowing
    let shadow_variable = 50; // Declares a variable named 'shadow_variable' with an initial value of 50
    let shadow_variable = "shadowed"; // Shadows the previous 'shadow_variable' with a new value
    println!("Value of shadow_variable: {}", shadow_variable); // Prints the value of the shadowed 'shadow_variable'
}
