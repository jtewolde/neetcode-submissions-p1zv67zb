class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # Approach: Use a greedy method to find the pair of elements in nums that are decreasing.
        # Then, determine which element in the curr pair needs to be changed, decreased left one or increase right one
        # If any element was changed, then switch boolean variable from false to true and vice versa

        # Initialize boolean variable for stroing if any elements in nums have changed
        changedResult = False

        # Iterate through each pair of elements in the nums array
        for indx in range(len(nums) - 1):
            # Check current pair to see if it is decreasing, if ture then continue with iteration
            if nums[indx] <= nums[indx + 1]:
                continue
            # Otherwise, if an element has been changed, then return False
            if changedResult == True:
                return False

            # First case of fixing violation: If the right element in pair exceed previous element
            # Then, set num at current index equal to right element by decreasing the larger element
            if indx == 0 or nums[indx + 1] >= nums[indx - 1]:
                nums[indx] = nums[indx + 1]
            # Otherwise, increase the smaller element on the pair
            else:
                nums[indx + 1] = nums[indx]
            changedResult = True
        return True