class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Approach: Use backtracking/Counter to get all of the permutations of how nums array is sorted
        # First, initialize variables/arrays needed for counting permutations of nums
        # Create ans array that will store all of the permutations
        # Perm array will store the current permuation of nums array that will be in ans
        # Use Counter data structure on nums to get the count of all numbers in nums
        # Then, create backtrack function to build the permutations in ans
        # Check if the len of the current permutation is the same length as nums array
        # If true, append the copy fo the current perm into the ans array
        # Iterate through the items in count hashset of Counter
        #
        
        # First, initialize variables/arrays needed for counting permutations of nums
        ans = []
        currPerm = []
        count = Counter(nums)

        # Then, create backtrack function to build the permutations in ans
        def backtrack():
            # Establish base case to see if current perm is same length of nums array
            if len(currPerm) == len(nums):
                ans.append(currPerm.copy())
                return

            # Iterate through every unique number that is in count
            for num in count:
                # Only use the number if the count is greater than zero
                if count[num] > 0:
                    # Choose: include the following number in the current permutation
                    currPerm.append(num)
                    count[num] -= 1

                    # Explore: use recursion to build out the rest of the permutation
                    backtrack()

                    # Backtrack to restore back to state
                    count[num] += 1
                    currPerm.pop()

        backtrack()
        return ans

