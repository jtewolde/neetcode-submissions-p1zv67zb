class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Goal: Convert/Sort the nums array so that the order of nums go back and forth from being greater and less than previous element
        # Example: [3, 5, 2, 4, 1, 9] -> +, -, +, -, +, -
        # Approach: Use a greedy approach where we iterate through every num in the array except the zero index
        # Swap two nums in array depending on if the current element is less or more than previous element
        # For odd, if curr element is less than prev element, swap their place in the array
        # For even, if curr element is greater than prev element, also swap those elements

        for indx in range(1, len(nums)):
            if ((indx % 2 == 1 and nums[indx] < nums[indx - 1]) or 
                (indx % 2 == 0 and nums[indx] > nums[indx - 1])):
                nums[indx], nums[indx - 1] = nums[indx - 1], nums[indx]