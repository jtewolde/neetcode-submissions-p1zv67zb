class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Goal: Find and return the unique elements from nums array without duplicates
        # Return the number of unique elements of nums
        # First approach: Convert nums array into sorted hashset to remove duplicates automatically
        # Runtime: O(N Log N5)

        # Convert nums array into hashSet that is sorted to remove duplicates
        numsSet = sorted(set(nums))
        # Replace elememts in nums array to new elements with no duplicates
        nums[:len(numsSet)] = numsSet
        # Return number of unique elements as K
        return len(numsSet)