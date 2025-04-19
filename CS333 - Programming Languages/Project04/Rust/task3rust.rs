// Differences from C:
// - Rust's generics and traits (like Ord for ordering) enable writing sort functions that work with any comparable type, unlike C's need for specific type implementations or void pointers with casting.
// - Rust's memory safety and array manipulation are more straightforward, reducing the risk of errors common in C.

// Generic bubble sort function that sorts any Vec<T> where T can be ordered and copied.
fn bubble_sort<T: PartialOrd + Copy>(mut arr: Vec<T>) -> Vec<T> {
    let mut n = arr.len();
    let mut swapped = true;
    
    // Continues looping until no swaps are made (array is sorted).
    while swapped {
        swapped = false;
        for i in 1..n {
            // Uses partial_cmp for comparison to handle types like float.
            if arr[i - 1].partial_cmp(&arr[i]).unwrap_or(std::cmp::Ordering::Less) == std::cmp::Ordering::Greater {
                arr.swap(i - 1, i); // Swaps elements if they are in the wrong order.
                swapped = true;
            }
        }
        n -= 1; // Decreases n since the last element is now sorted.
    }
    arr // Returns the sorted array.
}

fn main() {
    // Sorts an array of integers using the bubble_sort function.
    let int_arr = vec![4, 2, 3, 1, 5];
    let sorted_ints = bubble_sort(int_arr);
    println!("Sorted ints: {:?}", sorted_ints);

    // Sorts an array of floats using the bubble_sort function.
    let float_arr = vec![4.1, 2.2, 3.3, 1.4, 5.5];
    let sorted_floats = bubble_sort(float_arr);
    println!("Sorted floats: {:?}", sorted_floats);
}