class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Approach: Use Two pointers techinque to swap odd and even numbers positions in nums array
        # Initialize left and right pointers on opposite ends of the nums array
        # Check if number at left pointer is odd using mod % 2 != 0,
        # Swap with number at right pointer to get even number at start of array
        # Do the same for right pointer
        # Repeat until both pointers meet at the middle of nums array

        left, right = 0, len(nums) - 1

        if(len(nums) < 2):
            return nums

        while left <= right:
            print(nums)
            if nums[left] % 2 != 0:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        
        return nums
