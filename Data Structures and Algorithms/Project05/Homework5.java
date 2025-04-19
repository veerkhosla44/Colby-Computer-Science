import java.util.NoSuchElementException;

public class Homework5 {
    public static void main(String args[]) {
        double maxLoadFactor = 0.5; // Max Load Factor
        double resizeMultiplier = 2.0; // Resize Multiplier
        int initialBuckets = 5;  // Initial number of buckets
        
        // Initializes the hash table with the specified max load factor and resize multiplier
        ChainedHashTable<Integer, String> hashTable = new ChainedHashTable<>(maxLoadFactor, resizeMultiplier);
        
        // Resizes the hash table to the initial number of buckets
        hashTable = new ChainedHashTable<>(initialBuckets, maxLoadFactor, resizeMultiplier);

        int elementsToInsert = 10;  // Number of elements to insert
        for (int i = 0; i < elementsToInsert; i++) {
            // Inserts elements into the hash table
            hashTable.insert(i, "Value" + i);

            // Gets the current number of buckets
            int currentNumBuckets = hashTable.getCurrentNumBuckets();

            // Prints hash table information
            System.out.println("buckets " + currentNumBuckets +
                    ", elements " + hashTable.getSize() +
                    ", lf " + ((double) hashTable.getSize() / currentNumBuckets) +
                    ", max lf " + maxLoadFactor +
                    ", resize multiplier " + resizeMultiplier);
        }

        System.out.println("\n");
        System.out.println("--- Lookup Tests ---");

        // Successful lookup for an existing key
        int existingKey = 5;
        System.out.println("Lookup for key " + existingKey + ": " + hashTable.lookup(existingKey));

        // Unsuccessful lookup for a non-existing key
        int nonExistingKey = 20;
        System.out.println("Lookup for key " + nonExistingKey + ": " + hashTable.contains(nonExistingKey));

        System.out.println("\n");
    }
}
