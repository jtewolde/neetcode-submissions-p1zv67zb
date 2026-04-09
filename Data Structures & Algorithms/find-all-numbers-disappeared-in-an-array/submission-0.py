class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Brute force approach: Use hashset to get all of the numbers in the range from 1 to n
        # Tranverse through the entire hashset and remove all elements that are in nums
        # Return remaining elements in hashset as list
        
        # Initialize hashSet that has all numbers in the range [1, n]
        n = len(nums)
        hashSet = set(range(1, n + 1))

        # Remove all numbers that are originally in nums array
        # Leaving numbers that are missing
        for num in nums:
            hashSet.discard(num)

        return list(hashSet)