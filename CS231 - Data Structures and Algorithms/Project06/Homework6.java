public class Homework6 {

    // 1. Count Leaves
    private static int countLeavesHelper(BinaryTree.Node node) {
        // Base Case: If the node is null, there are no leaves.
        if (node == null) {
            return 0;
        }
        // If the node is a leaf, return 1.
        if (node.isLeaf()) {
            return 1;
        }
        // Reduction Step: Recursively count leaves in left and right subtrees.
        int leftLeaves = countLeavesHelper(node.getLeft());
        int rightLeaves = countLeavesHelper(node.getRight());
        return leftLeaves + rightLeaves;
    }

    public static int countLeaves(BinaryTree tree) {
        // Start the leaf counting process from the root.
        return countLeavesHelper(tree.getRoot());
    }

    // 2. Count Non-leaves
    private static int countNonLeavesHelper(BinaryTree.Node node) {
        // Base Case: If the node is null or a leaf, it's not a non-leaf.
        if (node == null || node.isLeaf()) {
            return 0;
        }
        // Reduction Step: Recursively count non-leaves in left and right subtrees.
        int leftNonLeaves = countNonLeavesHelper(node.getLeft());
        int rightNonLeaves = countNonLeavesHelper(node.getRight());
        return 1 + leftNonLeaves + rightNonLeaves;
    }

    public static int countNonLeaves(BinaryTree tree) {
        // Start the non-leaf counting process from the root.
        return countNonLeavesHelper(tree.getRoot());
    }

    // 3. Get Height
    private static int getHeightHelper(BinaryTree.Node node) {
        // Base Case: If the node is null, its height is 0.
        if (node == null) {
            return 0;
        }
        // Reduction Step: Recursively get height of left and right subtrees,
        // and return the maximum plus 1 (to include the current node).
        int leftHeight = getHeightHelper(node.getLeft());
        int rightHeight = getHeightHelper(node.getRight());
        return Math.max(leftHeight, rightHeight) + 1;
    }

    public static int getHeight(BinaryTree tree) {
        // Start calculating height from the root.
        return getHeightHelper(tree.getRoot());
    }

    // 4. Print Pre-Order
    public static void printPreOrderHelper(BinaryTree.Node node) {
        // Base Case: If the node is null, do nothing.
        if (node == null) {
            return;
        }
        // Print the current node's data.
        System.out.print(node.getData() + " ");
        // Recursively print left and right subtrees in pre-order.
        printPreOrderHelper(node.getLeft());
        printPreOrderHelper(node.getRight());
    }

    public static void printPreOrder(BinaryTree tree) {
        // Start pre-order traversal from the root.
        printPreOrderHelper(tree.getRoot());
    }

    // 5. Print In-Order
    public static void printInOrderHelper(BinaryTree.Node node) {
        // Base Case: If the node is null, do nothing.
        if (node == null) {
            return;
        }
        // Recursively print left subtree in-order.
        printInOrderHelper(node.getLeft());
        // Print the current node's data.
        System.out.print(node.getData() + " ");
        // Recursively print right subtree in-order.
        printInOrderHelper(node.getRight());
    }

    public static void printInOrder(BinaryTree tree) {
        // Start in-order traversal from the root.
        printInOrderHelper(tree.getRoot());
    }

    // 6. Print Post-Order
    public static void printPostOrderHelper(BinaryTree.Node node) {
        // Base Case: If the node is null, do nothing.
        if (node == null) {
            return;
        }
        // Recursively print left and right subtrees in post-order.
        printPostOrderHelper(node.getLeft());
        printPostOrderHelper(node.getRight());
        
        // Print the current node's data.
        System.out.print(node.getData() + " ");
    }

    public static void printPostOrder(BinaryTree tree) {
        // Start post-order traversal from the root.
        printPostOrderHelper(tree.getRoot());
    }

    // 7. Removes Leaves
    private static BinaryTree.Node removeLeavesHelper(BinaryTree.Node node) {
        // Base Case: If the node is null, return null.
        if (node == null) {
            return null;
        }
        // If the node is a leaf, remove it by returning null.
        if (node.isLeaf()) {
            return null;
        }
        // Recursively remove leaves in left and right subtrees.
        node.left = removeLeavesHelper(node.getLeft());
        node.right = removeLeavesHelper(node.getRight());
        return node;
    }

    public static void removeLeaves(BinaryTree tree) {
        // Start removing leaves from the root.
        removeLeavesHelper(tree.getRoot());
    }

    public static void main(String args[]) {
    // Initialize Tree1
        BinaryTree<Integer> tree1 = new BinaryTree<Integer>();
        tree1.insertRoot(1);
        tree1.getRoot().insertLeft(2);
        tree1.getRoot().insertRight(3);
        tree1.getRoot().getLeft().insertLeft(4);
        tree1.getRoot().getLeft().getLeft().insertLeft(7);
        tree1.getRoot().getRight().insertLeft(5);
        tree1.getRoot().getRight().insertRight(6);
        tree1.getRoot().getRight().getRight().insertRight(8);
        tree1.getRoot().getRight().getRight().getRight().insertRight(9);

        // Initialize Tree2
        BinaryTree<Integer> tree2 = new BinaryTree<Integer>();
        tree2.insertRoot(6);
        tree2.getRoot().insertLeft(4);
        tree2.getRoot().getLeft().insertRight(5);
        tree2.getRoot().getLeft().insertLeft(2);
        tree2.getRoot().getLeft().getLeft().insertLeft(1);
        tree2.getRoot().getLeft().getLeft().insertRight(3);
        tree2.getRoot().insertRight(8);
        tree2.getRoot().getRight().insertLeft(7);
        tree2.getRoot().getRight().insertRight(9);

        // 1.
        System.out.println("\n" + "---Number of leaf nodes---");
        System.out.println("Tree 1: " + countLeaves(tree1));
        System.out.println("Tree 2: " + countLeaves(tree2));

        // 2.
        System.out.println("\n" + "---Number of non-leaf nodes---");
        System.out.println("Tree 1: " + countNonLeaves(tree1));
        System.out.println("Tree 2: " + countNonLeaves(tree2));

        // 3.
        System.out.println("\n" + "---Height---");
        System.out.println("Tree 1: " + getHeight(tree1));
        System.out.println("Tree 2: " + getHeight(tree2));

        // 4.
        System.out.println("\n" + "---Pre-Order Traversal---");
        System.out.print("Tree 1: ");
        printPreOrder(tree1);
        System.out.println();
        System.out.print("Tree 2: ");
        printPreOrder(tree2);
        System.out.println();

        // 5.
        System.out.println("\n" + "---In-Order Traversal---");
        System.out.print("Tree 1: ");
        printInOrder(tree1);
        System.out.println();
        System.out.print("Tree 2: ");
        printInOrder(tree2);
        System.out.println();

        // 6.
        System.out.println("\n" + "---Post-Order Traversal---");
        System.out.print("Tree 1: ");
        printPostOrder(tree1);
        System.out.println();
        System.out.print("Tree 2: ");
        printPostOrder(tree2);
        System.out.println();

        // 7.
        System.out.println("\n" + "---Removes Leaves---");
        
        removeLeaves(tree1);

        System.out.println("Pre Order:");
        printPreOrder(tree1);
        System.out.println();

        System.out.println("In Order:");
        printInOrder(tree1);
        System.out.println();

        System.out.println("Post Order:");
        printPostOrder(tree1);

        System.out.println();
        System.out.println();

        removeLeaves(tree2);
        System.out.println("Pre Order:");
        printPreOrder(tree2);
        System.out.println();

        System.out.println("In Order:");
        printInOrder(tree2);
        System.out.println();

        System.out.println("Post Order:");
        printPostOrder(tree2);
    }
}
