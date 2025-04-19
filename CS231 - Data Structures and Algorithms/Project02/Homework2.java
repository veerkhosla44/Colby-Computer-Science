// import cse41321.containers.SinglyLinkedList;

public class Homework2 {
    public static void appendTerm(SinglyLinkedList<Double> polynomial,
                            Double coefficient) {
        polynomial.insertTail(coefficient);
    }
        

    public static void display(SinglyLinkedList<Double> polynomial) {
        int exp = polynomial.getSize() - 1;
        String poly = "";

        for (int i = 0; i < polynomial.getSize(); i++) {
            if (exp != 0) {
                poly += polynomial.getHead().getData() + "x^" + exp + " + ";
            }
            else {
                poly += polynomial.getHead().getData();
            }

            polynomial.insertTail(polynomial.getHead().getData());
            polynomial.removeHead();
            exp--;
        }
        System.out.println("Display:");
        System.out.println("------");    
        System.out.println(poly);
        System.out.println("");
    }

    public static Double evaluate(SinglyLinkedList<Double> polynomial, Double x) {
        Double result = 0.0;
        int exp = polynomial.getSize() - 1;

        for (int i = 0; i < polynomial.getSize(); i++){
            // Double coefficient = polynomial.getData();
            Double varTerm = 1.0;

            for (int j = 0; j < exp; j++) {
                varTerm *= x;
            }
            
        result += polynomial.getHead().getData() * varTerm;

        polynomial.insertTail(polynomial.getHead().getData());
        polynomial.removeHead();
        exp--;

        }
        System.out.println("Evaluation:");
        System.out.println("------");       
        System.out.println(result);
        System.out.println("");
        return result;
    }

    public static void main(String[] args) {
        System.out.println("Test 1:");
            SinglyLinkedList<Double> polynomial1 = new SinglyLinkedList<>();
            appendTerm(polynomial1, 1.0);
            appendTerm(polynomial1, 1.0);

            display(polynomial1);
            evaluate(polynomial1, 1.0);

        System.out.println("Test 2:");
            SinglyLinkedList<Double> polynomial2 = new SinglyLinkedList<>();
            appendTerm(polynomial2, 1.0);
            appendTerm(polynomial2, 0.0);
            appendTerm(polynomial2, -1.0);

            display(polynomial2);
            evaluate(polynomial2, 2.03);

        System.out.println("Test 3:");
            SinglyLinkedList<Double> polynomial3 = new SinglyLinkedList<>();
            appendTerm(polynomial3, -3.0);
            appendTerm(polynomial3, 0.5);
            appendTerm(polynomial3, -2.0);
            appendTerm(polynomial3, 0.0);

            display(polynomial3);
            evaluate(polynomial3, 5.0);

        System.out.println("Test 4:");
            SinglyLinkedList<Double> polynomial4 = new SinglyLinkedList<>();
            appendTerm(polynomial4, -0.3125);
            appendTerm(polynomial4, -9.915);
            appendTerm(polynomial4, -7.75);
            appendTerm(polynomial4, -40.0);
            appendTerm(polynomial4, 0.0);

            display(polynomial4);
            evaluate(polynomial4, 123.45);
    }
}