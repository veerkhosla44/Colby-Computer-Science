import java.util.Comparator;

public class Homework3 {
    public static class Car {
        public String make;
        public String model;
        public int mpg; // Miles per gallon

        public Car(String make, String model, int mpg) {
            this.make = make;
            this.model = model;
            this.mpg = mpg;
        }

        public String toString() {
            return "Car Make: " + this.make + ", Car Model: " + this.model + ", Miles Per Gallon: " + this.mpg;
        }
    }

    public static class CompareCarsByMakeThenModel implements Comparator<Car> {
        public int compare(Car car1, Car car2) {
            String car1make = car1.make;
            String car2make = car2.make;
            String car1model = car1.model;
            String car2model = car2.model;

            if (car1make.compareTo(car2make) == 0) {
                // If makes are the same, compare by model name
                return car1model.compareTo(car2model);
            } else {
                // Otherwise, compare by make name
                return car1make.compareTo(car2make);
            }
        }
    }

    public static class CompareCarsByDescendingMPG implements Comparator<Car> {
        public int compare(Car car1, Car car2) {
            int car1mpg = car1.mpg;
            int car2mpg = car2.mpg;

            // Sort in descending order based on MPG (Miles Per Gallon)
            return car2mpg - car1mpg;
        }
    }

    public static class CompareCarsByMakeThenDescendingMPG implements Comparator<Car> {
        public int compare(Car car1, Car car2) {
            String car1make = car1.make;
            String car2make = car2.make;
            int car1mpg = car1.mpg;
            int car2mpg = car2.mpg;

            if (car1make.compareTo(car2make) == 0) {
                // If makes are the same, sort in descending order based on MPG (Miles Per Gallon)
                return car2mpg - car1mpg;
            } else {
                // Otherwise, sort by make name in ascending order
                return car1make.compareTo(car2make);
            }
        }
    }

    public static void main(String args[]) {
        Car cars[] = {
                new Car("Toyota", "Camry", 33),
                new Car("Ford", "Focus", 40),
                new Car("Honda", "Accord", 34),
                new Car("Ford", "Mustang", 31),
                new Car("Honda", "Civic", 39),
                new Car("Toyota", "Prius", 48),
                new Car("Honda", "Fit", 35),
                new Car("Toyota", "Corolla", 35),
                new Car("Ford", "Taurus", 28)
        };

        // Print the unsorted list of cars
        System.out.println("");
        System.out.println("-------");
        System.out.println("Cars Unsorted:");
        for (int i = 0; i < cars.length; i++) {
            System.out.println(cars[i]);
        }

        // Sort the cars by make and then by model
        System.out.println("");
        System.out.println("-------");
        System.out.println("Cars Sorted By Make Then Model:");
        QuickSort.quickSort(cars, new CompareCarsByMakeThenModel());
        for (int i = 0; i < cars.length; i++) {
            System.out.println(cars[i]);
        }

        // Sort the cars in descending order based on MPG (Miles Per Gallon)
        System.out.println("");
        System.out.println("-------");
        System.out.println("Cars Sorted By Descending MPG:");
        QuickSort.quickSort(cars, new CompareCarsByDescendingMPG());
        for (int i = 0; i < cars.length; i++) {
            System.out.println(cars[i]);
        }

        // Sort the cars by make and then in descending order based on MPG
        System.out.println("");
        System.out.println("-------");
        System.out.println("Cars Sorted By Make Then Descending MPG:");
        QuickSort.quickSort(cars, new CompareCarsByMakeThenDescendingMPG());
        for (int i = 0; i < cars.length; i++) {
            System.out.println(cars[i]);
        }
    }
}
