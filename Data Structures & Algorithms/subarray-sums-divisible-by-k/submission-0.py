class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Approach: Use prefix sums and a hashmap to get the remainders of prefix sums when divided by k
        # Use the hashmap to count how many times each remainder appears and check if previous prefix sums share the same remainder
        # If two prefix sums have the same remainder, then the difference is also divisible by k as well.

        # Initialize needed variables like prefixSum for tracking current prefix sum at zero as well as ans
        # Then, create prefixCount hashmap for tracking remainders from dividing by k and put prefix sum of zero to count 1
        prefixSum, ans = 0, 0
        prefixCount = defaultdict(int)
        prefixCount[0] = 1 

        # Iterate through each number in nums array and add curr num into prefixSum and get the remainder of current prefixSum
        for num in nums:
            prefixSum += num
            remainder = prefixSum % k

            # Increment ans variable with the count of the current remainder for prefixSum
            # Then, increment remaninder count by one
            ans += prefixCount[remainder]
            prefixCount[remainder] += 1
        return ans