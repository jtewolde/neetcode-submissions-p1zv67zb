class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Initial approach of problem using Backtracking
        # Backtracking is essentially DFS, where instead of tranversing through a tree and nodes
        # You are traversing through different combinations of numbers in arrays, etc.
        # Think of backtracking like DFS -> Establish base case, use recursion on both possiblites, to or not to do, (left and right children)

        # Create ans variable array to keep track of entire array of subsets
        # Create subset variable array to keep track of current subset
        # Create modified DFS function where parameter is index of numberin array instead of node
        # Base case: If current index is out of bounds of len of nums, create a copy of current subset array and append to ans array and return
        # After, use recursion with DFS for the two decisions to be made when iterating through recurison tree
        # First decision: to add nums[index] to subset -> add nums[index] to subset array, then use DFS on next index
        # Second decision: not to add nums[index] to subset -> Pop out current subset then perform DFS on next index as well

        # Final Answer variable with all subsets in array
        ans = []
        subset = []

        def dfs(index):
            if index >= len(nums):
                ans.append(subset.copy())
                return

            subset.append(nums[index])
            dfs(index + 1)

            subset.pop()
            dfs(index + 1)

        dfs(0)
        return ans
