class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # The goal of this problem is to simply roate the contents of the array by the value of k
        # Meaning that the elements in the array will be shifted ro the right k times
        # Approach: Use a three-reversal approach where we first reverse the entire nums array
        # This happens so that the original right side of array is moved to the front of the array
        # Second, reverse the first k elements to make those elements in order
        # Third, Reverse the remaining n - k elements to restore the original order

        # Handle edge cases by using modulo operation to get effective rotation count
        n = len(nums)
        k = k % n

        # Create a helper function, reverse, that takes two pointers as the parameters
        def reverse(left: int, right: int):
            # Loop through lementsin from left ot right
            # Swap elements at positions that are at left and right pointers
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                # Move both pointers inward towards middle of array
                left += 1
                right -= 1

        # Apply three-reversal approach using the helper reverse function
        reverse(0, n - 1) # Reverse entire nums array
        reverse(0, k - 1) # Reverese the first k elements in the array
        reverse(k, n - 1) # Reverse the remaining elements


