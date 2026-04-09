class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # The goal os this problem is to see if all pairs of elements in nums array are a different parity
        # Meaning that one element is even and the other is odd
        # Approach: Iterate through then entire nums array, starting from index 1
        # Compare the previous element to the current element based on their parity
        # Check if both elementa re both even or odd, if the same > continue to iterate
        # If false, then return false

        # Starting from index 1, iterate through entire nums array
        for i in range(1, len(nums)):
            # Using modulo division, compare the result of mod 2 for current and previous element
            # If the result are not equal to both, then one element is even and one is odd
            if nums[i - 1] % 2 != nums[i] % 2:
                continue
            # Otherwise, return False for ht entire nums array
            else:
                return False

        return True