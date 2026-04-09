class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Approach for solving this problem using recursive backtracking
        # First, create two list variables, ans for final answer of all permutations
        # Second is sub for storing sub array of a single permutation
        # Create a backtrack function with no arguments where it will go through decision tree
        # Set a base case for function where if the length of a sublist is equal to the len of nums array
        # Append the copy of sublist to the ans array and return
        # Iterate through each number in nums array, if the curr num is not in the sublist,
        # Append the curr num to the sublist array and then call the backtrack function, then pop it out to backtrack

        ans = []
        sub = []
        n = len(nums)

        def backtrack():
            if len(sub) == n:
                ans.append(sub.copy())
                return

            for num in nums:
                if num not in sub:
                    sub.append(num)
                    backtrack()
                    sub.pop()

        backtrack()
        return ans

            