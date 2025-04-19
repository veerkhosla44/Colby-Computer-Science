/* Veer Khosla
CS333
3/17/24
Performs binary search on an array of numbers
*/


fn binary_search(arr: &[i32], target: i32) -> Option<usize> {
    let mut low = 0;
    let mut high = arr.len() - 1;

    while low <= high {
        let mid = low + (high - low) / 2;

        if arr[mid] == target {
            return Some(mid);
        } else if arr[mid] < target {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    None
}

fn main() {
    let arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20];
    let target = 12;

    if let Some(index) = binary_search(&arr, target) {
        println!("Target {} found at index {}", target, index);
    } else {
        println!("Target {} not found in the array", target);
    }
}