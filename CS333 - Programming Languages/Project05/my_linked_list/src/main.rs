mod linkedlist;
use linkedlist::LinkedList;

// Helper functions for integer operations
fn print_int(x: &mut i32) {
    println!("{}", *x);
}

fn square_int(x: &mut i32) {
    *x = *x * *x;
}

// Helper functions for float operations
fn print_float(x: &mut f32) {
    println!("{}", *x);
}

fn square_float(x: &mut f32) {
    *x = *x * *x;
}

fn main() {
    println!("TESTING INTEGER\n");
    let mut int_list = LinkedList::new();
    for i in (0..20).step_by(2).rev() {
        int_list.push(i);
    }

    println!("After initialization\n");
    int_list.map(print_int);

    println!("After squaring\n");
    int_list.map(square_int);
    int_list.map(print_int);

    println!("After append\n");
    int_list.append(30);
    int_list.map(print_int);

    println!("After clear\n");
    int_list.clear();
    int_list.map(print_int);

    println!("After append\n");
    for i in 0..5 {
        int_list.append(i);
    }
    int_list.map(print_int);

    println!("Popped {}\n", int_list.pop().unwrap_or(-1)); // using unwrap_or to handle empty case
    println!("Popped {}\n", int_list.pop().unwrap_or(-1));

    println!("After popping\n");
    int_list.map(print_int);
    println!("Size {}\n", int_list.size());

    println!("TESTING FLOAT\n");
    let mut float_list = LinkedList::new();
    for i in 0..10 {
        float_list.push(i as f32 + 0.5);
    }

    println!("After initialization\n");
    float_list.map(print_float);

    println!("After squaring\n");
    float_list.map(square_float);
    float_list.map(print_float);

    println!("After append\n");
    float_list.append(30.5);
    float_list.map(print_float);

    println!("After clear\n");
    float_list.clear();
    float_list.map(print_float);

    println!("After append\n");
    for i in 0..5 {
        float_list.append(i as f32 / 2.0);
    }
    float_list.map(print_float);

    println!("Popped {}\n", float_list.pop().unwrap_or(0.0)); // using unwrap_or to handle empty case
    println!("Popped {}\n", float_list.pop().unwrap_or(0.0));

    println!("After popping\n");
    float_list.map(print_float);
    println!("Size {}\n", float_list.size());
}
