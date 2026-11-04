class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # Approach: Solve this problem using Greedy to find the maximum possible score among all pairs.
        # Iterate through each value from left to right, keep track of max value of values[idx] + 1
        # Check each position once as a potential right endpoint while maintaining best possible left endpoint

        # Initialize tracking variables where ans stores max score found so far, initialized at 0
        # Also, initialize currMax that will track the current max, initialized with first value in values minus 1 for distance
        ans = 0
        curr_max = values[0] - 1

        # Iterate through each value, skipping first value 
        for idx in range(1, len(values)):
            ans = max(ans, values[idx] + curr_max)
            curr_max = max(curr_max - 1, values[idx] - 1)
        return ans

