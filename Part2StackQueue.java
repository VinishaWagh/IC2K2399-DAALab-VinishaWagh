import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class Part2StackQueue {

    public static void simulateStack(String[] tasks) {
        Stack<String> stack = new Stack<>();
        System.out.println("--- Stack Operations (LIFO) ---");
        for (String task : tasks) {
            stack.push(task);
            System.out.println("Pushed: " + task + " | Current Stack: " + stack);
        }

        StringBuilder completionOrder = new StringBuilder();
        while (!stack.isEmpty()) {
            String task = stack.pop();
            completionOrder.append(task).append(stack.isEmpty() ? "" : ", ");
            System.out.println("Popped: " + task + " | Remaining Stack: " + stack);
        }
        System.out.println("\nStack Order (LIFO): " + completionOrder);
    }

    public static void simulateQueue(String[] tasks) {
        Queue<String> queue = new LinkedList<>();
        System.out.println("\n--- Queue Operations (FIFO) ---");
        for (String task : tasks) {
            queue.add(task);
            System.out.println("Enqueued: " + task + " | Current Queue: " + queue);
        }

        StringBuilder completionOrder = new StringBuilder();
        while (!queue.isEmpty()) {
            String task = queue.poll();
            completionOrder.append(task).append(queue.isEmpty() ? "" : ", ");
            System.out.println("Dequeued: " + task + " | Remaining Queue: " + queue);
        }
        System.out.println("\nQueue Order (FIFO): " + completionOrder);
    }

    public static void main(String[] args) {
        String[] tasks = {"Task1", "Task2", "Task3", "Task4", "Task5"};
        System.out.println("Input Tasks: " + String.join(", ", tasks) + "\n");

        simulateStack(tasks);
        simulateQueue(tasks);

        System.out.println("\n--- Printer Requirement ---");
        System.out.println("Printer should use: Queue (FIFO)");
        System.out.println("Printer Print Order: Task1, Task2, Task3, Task4, Task5");
        System.out.println("Reason: A printer needs First-Come, First-Served fairness so that tasks print in arrival order.");
    }
}
