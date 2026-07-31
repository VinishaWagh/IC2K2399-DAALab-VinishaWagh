public class Part4Complexity {

    public static int singleLoop(int n) {
        int count = 0;
        for (int i = 1; i <= n; i++) {
            count++;
        }
        return count;
    }

    public static int nestedLoop(int n) {
        int count = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        // Case n = 5
        int single5 = singleLoop(5);
        int nested5 = nestedLoop(5);
        System.out.println("--- Loop Execution Counts for n = 5 ---");
        System.out.println("Single loop (i = 1 to 5) runs: " + single5 + " times");
        System.out.println("Nested loop (i = 1 to 5, j = 1 to 5) total prints: " + nested5 + " times");

        // Case n = 20 for single loop
        int single20 = singleLoop(20);
        System.out.println("\n--- Single Loop Execution for n = 20 ---");
        System.out.println("Single loop (i = 1 to 20) runs: " + single20 + " times");

        // Case n = 10 for both loops
        int single10 = singleLoop(10);
        int nested10 = nestedLoop(10);
        System.out.println("\n--- Loop Execution Counts for n = 10 ---");
        System.out.println("Single loop (i = 1 to 10) runs: " + single10 + " times");
        System.out.println("Nested loop (i = 1 to 10, j = 1 to 10) runs: " + nested10 + " times");

        System.out.println("\n--- Growth Analysis (Input size grew 100x) ---");
        System.out.println("Single Loop Growth: Proportionally (Linear O(n)). Effort scales linearly with input size n.");
        System.out.println("Nested Loop Growth: Explosively (Quadratic O(n^2)). Effort scales quadratically with input size n^2.");
    }
}
