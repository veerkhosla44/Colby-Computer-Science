public class Homework8 {
    public static boolean isExitReachable(Graph<Character, Integer> maze, char entrance, char exit) {

        // Initialize visited flag for each vertex in the graph
        for (Graph<Character, Integer>.Vertex vertex : maze.getVertices()) {
            vertex.getData().color = VertexColor.WHITE;
        }

        // Start the recursive search from the entrance
        return isExitReachableRecursive(maze, entrance, exit);
    }

    private static boolean isExitReachableRecursive(Graph<Character, Integer> maze, char current, char exit) {
        // Base Case: If we reach the exit, return true
        if (current == exit) {
            return true;
        }

        // Iterate through edges from the current room
        for (Graph<Character, Integer>.Edge edge : maze.getEdges(current)) {
            char adjacent = edge.getToVertex().getData();

            // If the adjacent room is unvisited, explore it
            if (maze.getVertex(adjacent).getData().color == VertexColor.WHITE) {
                // Recursively call isExitReachableRecursive with the adjacent room as the current room
                if (isExitReachableRecursive(maze, adjacent, exit)) {
                    return true; // If a path to the exit is found, return true
                }
            }
        }

        // If no path is found from the current room, return false
        return false;
    }

    
    public static void main(String args[]) {
        // Create Maze 1
        Graph<Character, Integer> graph1 = new Graph<Character, Integer>();

        Character a1 = 'A';
        Character b1 = 'B';     
        Character c1 = 'C';
        Character d1 = 'D';
        Character e1 = 'E';
        Character f1 = 'F';
        Character g1 = 'G';

        graph1.insertVertex(a1);
        graph1.insertVertex(b1);
        graph1.insertVertex(c1);
        graph1.insertVertex(d1);
        graph1.insertVertex(e1);
        graph1.insertVertex(f1);
        graph1.insertVertex(g1);

        graph1.insertEdge(a1, c1, 0);
        graph1.insertEdge(c1, a1, 0);

        graph1.insertEdge(c1, f1, 0);
        graph1.insertEdge(f1, c1, 0);

        graph1.insertEdge(f1, g1, 0);
        graph1.insertEdge(g1, f1, 0);
        
        graph1.insertEdge(a1, d1, 0);
        graph1.insertEdge(d1, a1, 0);

        graph1.insertEdge(d1, e1, 0);
        graph1.insertEdge(e1, d1, 0);

        graph1.insertEdge(e1, g1, 0);
        graph1.insertEdge(g1, e1, 0);

        graph1.insertEdge(d1, g1, 0);
        graph1.insertEdge(g1, d1, 0);

        graph1.insertEdge(d1, b1, 0);
        graph1.insertEdge(b1, d1, 0);

        // Create Maze 2
        Graph<Character, Integer> graph2 = new Graph<Character, Integer>();

        Character a2 = 'A';
        Character b2 = 'B';     
        Character c2 = 'C';
        Character d2 = 'D';
        Character e2 = 'E';
        Character f2 = 'F';
        Character g2 = 'G';

        graph2.insertVertex(a2);
        graph2.insertVertex(b2);
        graph2.insertVertex(c2);
        graph2.insertVertex(d2);
        graph2.insertVertex(e2);
        graph2.insertVertex(f2);
        graph2.insertVertex(g2);

        graph2.insertEdge(a2, c2, 0);
        graph2.insertEdge(c2, a2, 0);

        graph2.insertEdge(c2, f2, 0);
        graph2.insertEdge(f2, c2, 0);
        
        graph2.insertEdge(a2, d2, 0);
        graph2.insertEdge(d2, a2, 0);

        graph2.insertEdge(e2, g2, 0);
        graph2.insertEdge(g2, e2, 0);

        graph2.insertEdge(d2, b2, 0);
        graph2.insertEdge(b2, d2, 0);


        boolean isReachable1 = isExitReachable(graph1, 'A', 'G');
        System.out.println("Maze 1: " + isReachable1);

        boolean isReachable2 = isExitReachable(graph2, 'A', 'G');
        System.out.println("Maze 2: " + isReachable2);
    }

}
