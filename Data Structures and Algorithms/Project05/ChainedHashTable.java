// ChainedHashTable.java

import java.util.Iterator;
import java.util.NoSuchElementException;

public class ChainedHashTable<K, V> {
    // Table of buckets
    private SinglyLinkedList<KeyValuePair<K, V>>[] table;

    private int size;
    private double maxLoadFactor;
    private double resizeMultiplier;

    public ChainedHashTable(double maxLoadFactor, double resizeMultiplier) {
        this(997, maxLoadFactor, resizeMultiplier);  // A prime number of buckets
    }

    @SuppressWarnings("unchecked")
    public ChainedHashTable(int buckets, double maxLoadFactor, double resizeMultiplier) {
        // Create table of empty buckets
        table = new SinglyLinkedList[buckets];
        for (int i = 0; i < table.length; ++i) {
            table[i] = new SinglyLinkedList<KeyValuePair<K, V>>();
        }

        size = 0;
        this.maxLoadFactor = maxLoadFactor;  // Set the maximum load factor
        this.resizeMultiplier = resizeMultiplier;  // Set the resize multiplier
    }

    public void resize() {
        int newTableLength = (int)(table.length * resizeMultiplier);  // Calculate the new table length
        SinglyLinkedList<KeyValuePair<K, V>>[] newTable = new SinglyLinkedList[newTableLength];  // Create a new table with the new length
    
        // Initialize each bucket in the new table with an empty linked list
        for (int i = 0; i < newTable.length; ++i) {
            newTable[i] = new SinglyLinkedList<KeyValuePair<K, V>>();
        }
    
        // Rehash the existing key-value pairs and place them in the new table
        for (K key: this.keys()) {
            // Calculate the new bucket for the key using the multiplication method
            int currentBucketNum = (int)(table.length * ((Math.sqrt(5) - 1) / 2) * key.hashCode() % 1);
    
            // Look up the value associated with the key
            V val = lookup(key);
    
            // Create a new key-value pair and insert it into the corresponding bucket in the new table
            KeyValuePair<K, V> keyValue = new KeyValuePair<K, V>(key, val);
            newTable[currentBucketNum].insertHead(keyValue);
        }
    
        table = newTable;  // Update the hash table with the new table
    }
    
    public int getCurrentNumBuckets() {
        return table.length;  // Return the current number of buckets (length of the table)
    }
    
    public int getSize() {
        return size;
    }

    public boolean isEmpty() {
        return getSize() == 0;
    }

    public void insert(K key, V value) throws
            IllegalArgumentException,
            DuplicateKeyException {
        if (key == null) {
            throw new IllegalArgumentException("key must not be null");
        }
        if (contains(key)) {
            throw new DuplicateKeyException();
        }
        if (size + 1 > table.length * maxLoadFactor) {
            resize();
        }

        getBucket(key).insertHead(new KeyValuePair<K, V>(key, value));
        ++size;
    }

    public V remove(K key) throws
            IllegalArgumentException,
            NoSuchElementException {
        if (key == null) {
            throw new IllegalArgumentException("key must not be null");
        }

        // If empty bucket
        SinglyLinkedList<KeyValuePair<K, V>> bucket = getBucket(key);
        if (bucket.isEmpty()) {
            throw new NoSuchElementException();
        }

        // If at head of bucket
        SinglyLinkedList<KeyValuePair<K, V>>.Element elem = bucket.getHead();
        if (key.equals(elem.getData().getKey())) {
            --size;
            return bucket.removeHead().getValue();
        }

        // Scan rest of bucket
        SinglyLinkedList<KeyValuePair<K, V>>.Element prev = elem;
        elem = elem.getNext();
        while (elem != null) {
            if (key.equals(elem.getData().getKey())) {
                --size;
                return bucket.removeAfter(prev).getValue();
            }
            prev = elem;
            elem = elem.getNext();
        }

        throw new NoSuchElementException();
    }

    public V lookup(K key) throws
            IllegalArgumentException,
            NoSuchElementException {
        if (key == null) {
            throw new IllegalArgumentException("key must not be null");
        }

        // Scan bucket for key
        SinglyLinkedList<KeyValuePair<K, V>>.Element elem =
                getBucket(key).getHead();
        while (elem != null) {
            if (key.equals(elem.getData().getKey())) {
                return elem.getData().getValue();
            }
            elem = elem.getNext();
        }

        throw new NoSuchElementException();
    }

    public boolean contains(K key) {
        try {
            lookup(key);
        } catch (IllegalArgumentException ex) {
            return false;
        } catch (NoSuchElementException ex) {
            return false;
        }

        return true;
    }

    private SinglyLinkedList<KeyValuePair<K, V>> getBucket(K key) {
        // Multiplication method
        return table[(int)(table.length * ((Math.sqrt(5) - 1) / 2) * key.hashCode() % 1)];
        }

    private class KeysIterator implements Iterator<K> {
        private int remaining;  // Number of keys remaining to iterate
        private int bucket;     // Bucket we're iterating
        private SinglyLinkedList<KeyValuePair<K, V>>.Element elem;
                                // Position in bucket we're iterating

        public KeysIterator() {
            remaining = ChainedHashTable.this.size;
            bucket = 0;
            elem = ChainedHashTable.this.table[bucket].getHead();
        }

        public boolean hasNext() {
            return remaining > 0;
        }

        public K next() {
            if (hasNext()) {
                // If we've hit end of bucket, move to next non-empty bucket
                while (elem == null) {
                    elem = ChainedHashTable.this.table[++bucket].getHead();
                }

                // Get key
                K key = elem.getData().getKey();

                // Move to next element and decrement entries remaining
                elem = elem.getNext();
                --remaining;

                return key;
            } else {
                throw new NoSuchElementException();
            }
        }
    }

    public Iterable<K> keys() {
        return new Iterable<K>() {
            public Iterator<K> iterator() {
                return new KeysIterator();
            }
        };
    }
}
