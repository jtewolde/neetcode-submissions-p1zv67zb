class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # Problem: Given a nums array and a parameter pivot, partition and structure the nums array into three consecutive groups,
        # The values less than pivot, values equal to pivot, and values greater than pivot while preserving the original order of the values
        # Approach: Use a two pointers approach where it iterates through nums array from left to right and vice versa
        
        # Initialize left and right pointers for iterating through nums array from both directions
        # Also, create pointers for inserting values into the ans array
        # Then, create ans array that is initialized with zeros with length of nums
        left, right = 0, len(nums) - 1
        i2, j2 = 0, len(nums) - 1
        ans = [0] * len(nums)

        # Iterate through the nums array until left pointer reaches the end of nums
        while left < len(nums):
            # Determine if current num at left pointer is less or greater than pivot value
            # If less, then set index in ans array to curr num at left and increment i2 to next index in ans
            if nums[left] < pivot:
                ans[i2] = nums[left]
                i2 += 1
            # If greater, then set index in ans array to curr num at right and decrement i2 to next index in ans
            if nums[right] > pivot:
                ans[j2] = nums[right]
                j2 -= 1
            # Move both pointers towards center of nums array with increment and decrement
            left, right = left + 1, right - 1
        
        # Get the elements that are equal to the pivot value
        while i2 <= j2:
            ans[i2] = ans[j2] = pivot
            i2, j2 = i2 + 1, j2 - 1
        return ans