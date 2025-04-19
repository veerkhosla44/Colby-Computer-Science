import java.util.Random;

public class Homework1 {
    // Insert an element at a specified index in the array
    public static int[] insert(int[] array, int index, int value) { // O(N)
        int[] newArray = new int[array.length + 1]; // Create a new array with length increased by 1
       
        // Copy elements before the specified index from the original array to the new array
        for (int i = 0; i < index; ++i) {
            newArray[i] = array[i]; // O(1)
        }

        newArray[index] = value; // Insert the new value at the specified index

        // Copy remaining elements from the original array to the new array, shifting them to the right
        for (int i = index; i < array.length; ++i) {
            newArray[i + 1] = array[i]; // O(1)
        }

        // returns the modified array 
        return newArray; // O(1)
    }
    
    public static void main(String args[]) {
        Random rand = new Random();

        final double NANO_SECONDS_PER_SECOND = 1000000000.0; // O(1)
        int numReadings = 60; // O(1)
        int insertsPerReading = 1000; // O(1)

        int[] testArray = {0};

        System.out.println("Array Length:\t\tSeconds Per Insert:");

        for (int i = 0; i < numReadings; ++i) { // O(numReadings)
            long startTime = System.nanoTime(); // O(1)

            for (int j = 0; j < insertsPerReading; ++j) { // O(insertsPerReading)
                int index = rand.nextInt(testArray.length); // O(1)
                int value = rand.nextInt(); // O(1)
                testArray = Homework1.insert(testArray, index, value); // O(N)
            }

            long stopTime = System.nanoTime(); // O(1)
            double timePerInsert = (stopTime - startTime) / NANO_SECONDS_PER_SECOND / insertsPerReading; // O(1)

            System.out.println((insertsPerReading * (i + 1)) + "\t\t\t" + timePerInsert); // O(1)
        }
    }
}
