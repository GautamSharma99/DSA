class Solution {

    public int search(int[] nums, int target) {

        int pivot = binarySearchfindpivot(nums);

        // Array not rotated
        if(pivot == -1) {
            return binarySearch(nums, 0, nums.length - 1, target);
        }

        // Pivot itself is target
        if(nums[pivot] == target) {
            return pivot;
        }

        // Search in left half
        if(target >= nums[0]) {
            return binarySearch(nums, 0, pivot - 1, target);
        }

        // Search in right half
        return binarySearch(nums, pivot + 1, nums.length - 1, target);
    }

    
    // Find pivot index
    public int binarySearchfindpivot(int[] nums) {

        int start = 0;
        int end = nums.length - 1;

        while(start <= end) {

            int mid = start + (end - start) / 2;

            // Case 1
            if(mid < end && nums[mid] > nums[mid + 1]) {
                return mid;
            }

            // Case 2
            if(mid > start && nums[mid] < nums[mid - 1]) {
                return mid - 1;
            }

            // Left side sorted
            if(nums[start] <= nums[mid]) {
                start = mid + 1;
            }

            // Right side sorted
            else {
                end = mid - 1;
            }
        }

        return -1;
    }

    
    // Normal Binary Search
    public int binarySearch(int[] nums, int start, int end, int target) {

        while(start <= end) {

            int mid = start + (end - start) / 2;

            if(nums[mid] == target) {
                return mid;
            }

            else if(nums[mid] < target) {
                start = mid + 1;
            }

            else {
                end = mid - 1;
            }
        }

        return -1;
    }
}