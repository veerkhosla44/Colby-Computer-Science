/*Veer Khosla
CS333
04/24/24
Defines a word counter that counts the number of occurrences of every word in a text file
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>


// Structure to store each word with its count
typedef struct {
    char word[100];
    int count;
} WordCount;

// Comparator for sorting words by their frequency
int compare_count(const void *a, const void *b) {
    WordCount *first = (WordCount *) a;
    WordCount *second = (WordCount *) b;
    return second->count - first->count; // Descending order
}

int main(int argc, char *argv[]) {
    // Ensure the correct usage
    if (argc != 2) {
        printf("Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    FILE *fp = fopen(argv[1], "r");
    if (!fp) {
        printf("Failed to open file %s\n", argv[1]);
        return 1;
    }

    WordCount words[10000];
    int num_words = 0;
    char buffer[100];

    // Read words from file
    while (fscanf(fp, "%99s", buffer) == 1) {
        // Clean up the word - remove punctuation and convert to lower case
        int length = strlen(buffer);
        for (int i = 0; i < length; i++) {
            if (ispunct(buffer[i])) {
                buffer[i] = '\0';
                length = i;
                break;
            }
            buffer[i] = tolower(buffer[i]);
        }

        int found = 0;
        for (int i = 0; i < num_words; i++) {
            if (strcmp(words[i].word, buffer) == 0) {
                words[i].count++;
                found = 1;
                break;
            }
        }

        if (!found) {
            strncpy(words[num_words].word, buffer, sizeof(words[num_words].word) - 1);
            words[num_words].word[sizeof(words[num_words].word) - 1] = '\0';
            words[num_words].count = 1;
            num_words++;
        }
    }

    fclose(fp);

    // Sort words by frequency
    qsort(words, num_words, sizeof(WordCount), compare_count);

    // Print the top 20 words
    printf("Top 20 words:\n");
    for (int i = 0; i < 20 && i < num_words; i++) {
        printf("%s: %d\n", words[i].word, words[i].count);
    }

    return 0;
}
