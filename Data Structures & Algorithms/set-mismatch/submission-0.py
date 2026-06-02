class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Approach: Use counter/hashmap to count the frequency of each number in nums
        # Iterate through all numbers ranging from 1 to len(nums) + 1 or n
        # Determine if current number appears in counter, if so replace first
        # Return an array where the first index is the repeating num and the second index is the missing num
        
        # Initialize Counter structure to count the frequency of each number in nums array
        # Also, create ans array that will store the repeating/missing nums.
        # Be default, it is [0, 0]
        count = Counter(nums)
        ans = [0,0]
        n = len(nums)

        # Iterate through all numbers ranging from 1 to n + 1
        for indx in range(1, n + 1):
            # Determine if current number appears in counter
            # If so, replace 1-index with missing num
            if count[indx] == 0:
                ans[1] = indx
            # Otherwise, if count of current num appears twice, then replace zero-index with current num
            elif count[indx] == 2:
                ans[0] = indx
        return ans