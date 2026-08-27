class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # Approach: Use a prefix sum approach where it tracks the current sum of subarray
        # Track the count of odd and even prefix sums to add to updating ans array

        # Initialize all needed variables like odd and even counts for counting number of prefix arrays
        # Also, create currSum to track the current sum of prefix array and ans variable for tracking num of subarrays
        # Then, create MOD variable for large answers to mod ans with
        currSum = oddCount = evenCount = ans = 0
        MOD = 10**9 + 7

        # Iterate through each element inside of arr
        for num in arr:
            # Increment currSum with current number from iteration
            currSum += num
            # If the current prefix sum is odd, then add 1 to ans for start of subarray 
            # Also, add the count of previous even prefix sums MOD with value
            if currSum % 2 == 1:
                ans = (ans + 1 + evenCount) % MOD
                oddCount += 1
            # If the current prefix sum is even, then do the same with ans variable but with oddCount and without adding 1
            # Also, increment evenCount by 1
            else:
                ans = (ans + oddCount) % MOD
                evenCount += 1
        return ans

        