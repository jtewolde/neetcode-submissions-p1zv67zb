class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Approach: Use backtracking and recursion to explore/build all combinations
        # First, initialize ans array for storing all valid combinations
        # Create a helper backtrack function that takes an start index and combination array as parameters
        # See if the length of combiantion array equals k for valid length of array
        # If true, append the copy of the comb array into ans and return
        # Next, create for loop starting from start index to n for iterating all numbers
        # For each number considered, append it to the combination array
        # Then, backtrack and use recursion to consider larger numbers for combinations
        # Pop last element from the comb array to backtrack before attempting next number

        # First, initialize ans array for storing all valid combinations
        ans = []

        # Create a helper backtrack function that takes an start number and combination array as parameters
        def backtrack(start, comb):
            # See if the length of combiantion array equals k for valid length of array
            # If true, append the copy of the comb array into ans and return
            if len(comb) == k:
                ans.append(comb.copy())

            # Next, create for loop starting from start index to n for iterating all numbers
            for num in range(start, n + 1):
                # For each number considered, append it to the combination array
                comb.append(num)
                # Then, backtrack and use recursion to consider larger numbers for combinations
                backtrack(num + 1, comb)
                # Pop last element from the comb array to backtrack before attempting next number
                comb.pop()

        backtrack(1, [])
        return ans

