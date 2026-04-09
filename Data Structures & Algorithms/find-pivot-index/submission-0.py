class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Approach: Use Prefix Sum to calculate both LHS and RHS of pivot to find pivot
        # First, create a total variable that has the total sum of nums array
        # Iterate through nums array, for every index, calculate RHS by taking difference of total - LHS - current element
        # Compare LHS to RHS to see if they are equivalent, if so, return that index as it is the pviot
        # If not, add current element to LHS and continue to next 

        # Initialize totalSum that has sum of all elements in nums
        # LHS for sum of elements left of pivot index
        totalSum = sum(nums)
        LHS = 0

        # Iterate through nums array
        for indx in range(len(nums)):
            # Calculate RHS by taking difference of total, LHS, and current element
            RHS = totalSum - LHS - nums[indx]

            # Pivot Index is found if both sums are equal
            if LHS == RHS:
                return indx

            # Update LHS if pivot index is not found, move to next element
            LHS += nums[indx]

        # No valid pivot index found
        return -1
             
