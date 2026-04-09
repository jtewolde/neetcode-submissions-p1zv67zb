class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Pseudo Code for hashmap solution:
        # Initialize a hast map to take value and index of num in nums array
        # Iterate through hashmap with index,num by enumerating through nums
        # Find the difference between one number and the target
        # IF the difference is in the hashmap currently, return solution
        # Else, Add current number to the hashmap and return

        prevMap = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], index]
            prevMap[num] = index
        return