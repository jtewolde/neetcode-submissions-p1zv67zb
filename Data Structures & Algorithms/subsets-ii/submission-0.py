class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Approach with solving this problem with backtracking
        # Create one variable, ans for final answer of arrays
        # Sort nums array to be able to skip duplicates 
        # Create a backtrack function, where it takes the index and a sublist as the parameters
        # Inside of function, initialize base case where if the index is equal to the length of nums
        # Append a copy of the sublist to ans array and return
        # Create two recursive scenarios for if sublist has nums[i] or doen't have sublist[i]
        # For scenario #1 where nums[i] is in sublist:
        # Append nums[i] to sublist array
        # Call backtrack function for next index using same sublist
        # Then, pop number from subset
        # For scenairo #2, where nums[i] isn't included in the sublist
        # Create a while loop where index + 1 is less thatn len of nums and if nums[index] == nums[index + 1]
        # Inside loop: increment index by 1
        # Then, call backtrack function the same as previously
        # Outside of backtrack function, call it with parameters being 0 for index and an empty list for sublist
        # Return ans as final result

        ans = []
        nums.sort()

        def backtrack(index, sublist):
            if index == len(nums):
                ans.append(sublist.copy())
                return

            # Scenario #1, using nums[index] inside of sublist
            sublist.append(nums[index])
            backtrack(index + 1, sublist)
            sublist.pop()

            # Scenario #2, not using nums[index] inside of sublist
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1

            backtrack(index + 1, sublist)

        backtrack(0, [])
        return ans


















