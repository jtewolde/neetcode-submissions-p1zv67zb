class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Synposis: Find and return all subarrays of nums array that equal the value of K
        # Brute Force Approach: Use a nested for loop to iterate through all combinations of numbers
        # For each num, find sequence of nums which sum will equal to k

        # Optimal Approach: Using a hash map and prefix approach to get subarrays
        # If sum of elements in subarray are equal, add to count that tracks answer
        # Prefix sum of a subarray is calculated by taking sum of current window minus k
        # If the prefix val is not in hashmap, add to hashmap

        # Initialize prefixSum Hashmap that stores frequencies of prefix sums
        # Ans variable to keep track of subarrays that equal k
        # cursum variable to keeping track of running prefix sum
        prefixSum = {0 : 1}
        ans = 0
        curSum = 0

        # Iterate through every number in nums array
        for num in nums:
            # Update curSum by adding with current number
            curSum += num
            # Calculate diff between curSum and the value of k
            diff = curSum - k
            # Check if the difference already exists in prefixSum hashmap,
            # If so, there are subarrays that ending at current index whose sum equals k
            # If not, return zero if the prefix doesn't exist in hashmap
            ans += prefixSum.get(diff, 0)

            # Add current prefixSum to the hashmap
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)

        return ans





            