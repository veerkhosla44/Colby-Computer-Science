use rayon::prelude::*;
use std::fs::File;
use std::io::{self, Read};
use std::sync::Mutex;
use std::time::Instant;

fn load_data(filename: &str) -> io::Result<Vec<f64>> {
    let mut file = File::open(filename)?;
    let mut buffer = Vec::new();
    file.read_to_end(&mut buffer)?;

    let n = buffer.len() / std::mem::size_of::<f64>();
    let mut data = vec![0.0; n];
    for i in 0..n {
        data[i] = f64::from_ne_bytes(buffer[i * 8..(i + 1) * 8].try_into().unwrap());
    }

    Ok(data)
}

fn leading_digit(n: f64) -> u8 {
    if n.abs() < 1.0 {
        let mut temp = n.abs();
        while temp < 1.0 {
            temp *= 10.0;
        }
        temp as u8
    } else {
        let mut temp = n.abs() as u64;
        while temp >= 10 {
            temp /= 10;
        }
        temp as u8
    }
}

fn main() {
    let filename = "longer.bin"; // Change as needed
    let data = load_data(filename).expect("Failed to load data");

    let counts = Mutex::new([0; 10]);

    let start = Instant::now();
    
    data.par_iter().for_each(|&value| {
        let digit = leading_digit(value);
        let mut counts = counts.lock().unwrap();
        counts[digit as usize] += 1;
    });

    let duration = start.elapsed();
    println!("Elapsed time: {:.4?} seconds", duration);

    let counts = counts.lock().unwrap();
    for i in 1..10 {
        println!("Digit {}: {}", i, counts[i]);
    }
}
