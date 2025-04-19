public class Homework4 {
    public static void addLargeNumbers (String num1, String num2) {
        Stack<Integer> stack1= new Stack<>();
        Stack<Integer> stack2= new Stack<>();

        for (int i = 0; i < num1.length(); i++) {
            stack1.push(Character.getNumericValue((num1.charAt(i))));
        }

        for (int i = 0; i < num2.length(); i++) {
            stack2.push(Character.getNumericValue((num2.charAt(i))));
        }

        Stack<Integer> resultStack = new Stack<>();
        int carry = 0;

        while (!stack1.isEmpty() || !stack2.isEmpty()) {
            int result = 0;

            int stack1pop;
            int stack2pop;

            if (!stack1.isEmpty()) {
                stack1pop = stack1.pop();
            }
            else {
                stack1pop = 0;
            }

            if (!stack2.isEmpty()) {
                stack2pop = stack2.pop();
            }
            else {
                stack2pop = 0;
            }

            result = stack1pop + stack2pop + carry;
            carry = 0;
            
            if (result > 9) {
                carry = 1;
                resultStack.push(result - 10);
            }
            else {
                resultStack.push(result);
            }
        }
        if (carry != 0) {
            resultStack.push(carry);
        }


        String output = "Expected Output: ";

        while (!resultStack.isEmpty()) {
            int resultStackPop = resultStack.pop();
            output += resultStackPop;
        }

        System.out.println(output);
    }

    public static void main(String args[]) {
        Homework4.addLargeNumbers("9223372036854775808", "12345678901234567890");
        Homework4.addLargeNumbers("9623372036854775807", "64837593764589374839");
        Homework4.addLargeNumbers("99999999999999999999", "11111111111111111111");
    }
}
