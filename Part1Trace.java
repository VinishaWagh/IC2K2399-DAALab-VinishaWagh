import java.util.Arrays;

public class Part1Trace {

    public static void findMaximum(int[] arr) {
        int maxVal = arr[0];
        int comparisons = 0;
        System.out.println("--- Dry Run: Finding Max ---");
        for (int i = 1; i < arr.length; i++) {
            comparisons++;
            int current = arr[i];
            if (current > maxVal) {
                maxVal = current;
            }
            System.out.println("i = " + i + ", A[i] = " + current + ", max = " + maxVal + ", comparisons = " + comparisons);
        }
        System.out.println("\nLargest Number: " + maxVal);
        System.out.println("Total Comparisons Made: " + comparisons);
    }

    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        int[] arrCopy = Arrays.copyOf(arr, n);
        System.out.println("\n--- Dry Run: Sorting (Bubble Sort) ---");
        int stepNum = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arrCopy[j] > arrCopy[j + 1]) {
                    int temp = arrCopy[j];
                    arrCopy[j] = arrCopy[j + 1];
                    arrCopy[j + 1] = temp;
                    System.out.println("Step " + stepNum + ": Swap " + arrCopy[j + 1] + " and " + arrCopy[j] + " -> " + Arrays.toString(arrCopy));
                } else {
                    System.out.println("Step " + stepNum + ": Compare " + arrCopy[j] + " and " + arrCopy[j + 1] + " (No Swap) -> " + Arrays.toString(arrCopy));
                }
                stepNum++;
            }
        }
        System.out.println("\nSorted Output: " + Arrays.toString(arrCopy));
    }

    public static void main(String[] args) {
        int[] givenList = {8, 3, 15, 6, 2};
        System.out.println("Input: " + Arrays.toString(givenList));
        findMaximum(givenList);
        bubbleSort(givenList);
    }
}
