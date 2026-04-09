class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Hash Set soltuion
        # Create a dictionary, go through nums,
        # If nums[i] isn't in dictionary, add it there
        # If nums[i] is in dictionary, return false

        result_set = set()

        for num in nums:
            if num in result_set:
                return True
            result_set.add(num)

        return False


         