/*Veer Khosla
CS333
04/24/24
Defines a word counter that counts the number of occurrences of every word in a text file
*/

use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead, BufReader};

fn main() -> io::Result<()> {
    let filename = "wctest.txt"; // Specify your input file here
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let mut word_count = HashMap::new();

    for line in reader.lines() {
        let line = line?;
        let words = line.split_whitespace()
            .map(|word| word.trim_matches(|c: char| !c.is_alphabetic()).to_lowercase());

        for word in words {
            if !word.is_empty() {
                *word_count.entry(word).or_insert(0) += 1;
            }
        }
    }

    // Sorting and printing top 20 words
    let mut word_vec: Vec<_> = word_count.into_iter().collect();
    word_vec.sort_by(|a, b| b.1.cmp(&a.1));

    for (word, count) in word_vec.iter().take(20) {
        println!("{}: {}", word, count);
    }

    Ok(())
}