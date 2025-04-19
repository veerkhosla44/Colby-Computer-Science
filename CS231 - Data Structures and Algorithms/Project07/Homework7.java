import java.util.Comparator;

public class Homework7 {
    public static class Person {
        String name;
        int age;
        double height;

        public Person(String name, int age, double height) {
            this.name = name;
            this.age = age;
            this.height = height;
        }

        public String toString() {
            return ("Person: " + this.name + ", Age: " + this.age + ", Height: " + this.height);
        }
    }

    // Comparator for sorting people by ascending name
    public static class ComparePeopleByAscendingName implements Comparator<Person> {
        public int compare(Person person1, Person person2) {
            // Compare names in ascending order
            return person1.name.compareTo(person2.name);
        }
    }

    // Comparator for sorting people by ascending age
    public static class ComparePeopleByAscendingAge implements Comparator<Person> {
        public int compare(Person person1, Person person2) {
            // Compare ages in ascending order
            return person1.age - person2.age;
        }
    }

    // Comparator for sorting people by ascending height
    public static class ComparePeopleByAscendingHeight implements Comparator<Person> {
        public int compare(Person person1, Person person2) {
            // Compare heights in ascending order
            if (person1.height == person2.height) {
                return 0;
            } else if (person1.height > person2.height) {
                return 1;
            } else {
                return -1;
            }
        }
    }

    // Method to sort an array of Person objects using a given comparator
    public static Person[] outputSorted(Person people[], Comparator<Person> comparator) {
        Heap<Person> heap = new Heap<>(comparator);
        for (int i = 0; i < people.length; i++) {
            heap.insert(people[i]);
        }

        Person outputArray[] = new Person[people.length];

        for (int i = 0; i < people.length; i++) {
            outputArray[i] = heap.extract();
        }

        return outputArray;
    }

    public static void main(String args[]) {

        // Array of Person objects
        Person people[] = {
            new Person("Veer", 19, 5.8),
            new Person("Edward", 20, 5.11),
            new Person("Jackie", 21, 5.4),
            new Person("Bryan", 20, 6.0),
            new Person("Gobs", 15, 5.6),
        };

        // Print unsorted array of people
        System.out.println("");
        System.out.println("People Unsorted:");
        for (int i = 0; i < people.length; i++) {
            System.out.println(people[i]);
        }

        System.out.println("");

        // Sort and print people by name
        System.out.println("People Sorted by Name:");
        Person outputArray[] = outputSorted(people, new ComparePeopleByAscendingName());
        for (int i = 0; i < outputArray.length; i++) {
            System.out.println(outputArray[i]);
        }

        System.out.println("");

        // Sort and print people by age
        System.out.println("People Sorted by Age:");
        outputArray = outputSorted(people, new ComparePeopleByAscendingAge());
        for (int i = 0; i < outputArray.length; i++) {
            System.out.println(outputArray[i]);
        }

        System.out.println("");

        // Sort and print people by height
        System.out.println("People Sorted by Height:");
        outputArray = outputSorted(people, new ComparePeopleByAscendingHeight());
        for (int i = 0; i < outputArray.length; i++) {
            System.out.println(outputArray[i]);
        }

        System.out.println("");
    }
}
