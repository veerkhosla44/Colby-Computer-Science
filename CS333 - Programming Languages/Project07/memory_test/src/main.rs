fn main() {
    use std::time::{Duration, Instant};

        let mut durations = Vec::new();
        for _ in 0..1000 {
            let start = Instant::now();
            let data = Box::new([0u8; 1000000]); // large allocation
            drop(data); // explicit deallocation
            let duration = start.elapsed();
            durations.push(duration);
        }
    
        let avg_duration: Duration = durations.iter().sum::<Duration>() / durations.len() as u32;
        println!("Average deallocation time: {:?}", avg_duration);
    }
