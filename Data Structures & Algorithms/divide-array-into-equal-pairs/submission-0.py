class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # Approach: Use a hashset structure that stores numbers while iterating through array
        # First, Initialize hashset strucutre that will be used to store a number at first c ocurance in array
        # If encountering a number is already in the hashset, then, remove from the set to complete pair
        # If the hashset is empty, then all pairs were created and return true
        # Otherwise, return false if there is a number that doesn't have a pair value

        # First, Initialize hashset strucutre that will be used to store a number at first occurance in array
        hashSet = set()

        # Iterate through entire nums array
        # If encountering a number is already in the hashset, then, remove from the set to complete pair
        for i in range(len(nums)):
            if nums[i] in hashSet:
                hashSet.remove(nums[i])
            elif nums[i] not in hashSet:
                hashSet.add(nums[i])

        # If the hashset is empty, then all pairs were created and return true
        # Otherwise, return false if there is a number that doesn't have a pair value
        return len(hashSet) == 0

        