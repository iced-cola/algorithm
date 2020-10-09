public class BinarySearch {
	public static int find(int[] arr, int key) {
        int lower = 0;
        int upper = arr.length - 1;
        while (true) {
            int curr = (lower + upper) / 2;
            if (arr[curr] == key) {
                return curr;
            } else if (lower > upper) {
                return -1;
            } else {
                if (arr[curr] > key) {
                    upper = curr - 1;
                } else {
                    lower = curr + 1;
                }
            }
        }
    }
}

