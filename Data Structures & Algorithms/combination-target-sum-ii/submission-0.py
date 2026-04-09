class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Initial Approach for solving this problem using Backtracking
        # Difference between Comb Sum 1 is that duplicate combinations can't be counted
        # EX: [2,2,2,2] for target 8

        # Create two lists, ans array for final answer of all combination sums, and sublist for sublists of answers
        # Sort the candidates array to help with identifying duplicates in array
        # Create a Backtrack helper function where it takes a index and current sum as a argument
        # Similar to DFS, establish two base cases where backtracking stops
        # Base Case 1: If current sum is equal to target, append sublist.copy() to ans list and return
        # Base Case 2: If current sum > target or the index is equal to len(nums), just return
        # Initialize two different scenairos of decision tree of using or not using same number
        # If not using same number, call backtrack function with new index(cur index + 1) and current sum
        # Append the new number(nums[i]) to ret sublist
        # If using same number, call backtrack function with same index but add current number to current sum
        # Pop number from sublist
        # Outside of Backtrack function, call it using both zeros as arguments
        # Return ans as final answer

        ans = []
        sublist = []
        candidates.sort()
        nums = candidates
        n = len(nums)

        def backtrack(index, cur_sum):
            # Base cases
            if cur_sum == target:
                ans.append(sublist.copy())
                return
            if cur_sum > target or index == n:
                return

            sublist.append(nums[index])

            # Decision to use same number
            backtrack(index + 1, cur_sum + nums[index])
            sublist.pop()

            # Decision to use new number by skipping duplicates of number
            # [1,1,1,1,2] -> skip all ones to get new number of 2
            while index + 1 < n and nums[index] == nums[index+1]:
                index += 1
            
            backtrack(index + 1, cur_sum)

        backtrack(0,0)
        return ans


            











