class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Approach: Use Two pointers techinque to swap odd and even numbers positions in nums array
        # Initialize left and right pointers on opposite ends of the nums array
        # Check if number at left pointer is odd using mod % 2 != 0,
        # Swap with number at right pointer to get even number at start of array
        # Do the same for right pointer
        # Repeat until both pointers meet at the middle of nums array

        # Initialize left and right pointers at opposite ends of nums array
        left, right = 0, len(nums) - 1

        # Establish edge case for there is only one element, return that element
        if(len(nums) < 2):
            return nums

        # Traverse through nums array with two pointers until they meet at middle
        while left <= right:
            # If the element at left pointer is odd, swap the numbers at left and right pointers
            if nums[left] % 2 != 0:
                nums[left], nums[right] = nums[right], nums[left]
                # Decrement right pointer more inside of nums array
                right -= 1
            else:
                # Otherwise, move to next number at left side of array
                left += 1
        
        return nums
