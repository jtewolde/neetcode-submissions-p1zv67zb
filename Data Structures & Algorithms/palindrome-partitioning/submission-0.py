class Solution:
    def partition(self, s: str) -> List[List[str]]:
    # Approach for solving this problem is with using Backtracking and helper function
    # Goal: Partition the given string s so that the output are strings that are palindromes and valid
    
        # Initialize two arrays, part for tracking current partition and ans for final answer that stores all partitions
        part = []
        ans = []

        # Create dfs function that takes index as the argument
        def dfs(indx):
            # Establish base case if the current index is out of bounds of string
            # If so, append a copy of part array to ans array
            if indx >= len(s):
                ans.append(part.copy())
                return
            
            # Process the next character in the string to see if both caracters on indx and next make a palidrome
            for next_indx in range(indx, len(s)):
                # Use helper function to determine if partition is a palidrome
                if self.isPali(s, indx, next_indx):
                    # Add valid partition to part array
                    part.append(s[indx: next_indx + 1])
                    dfs(next_indx + 1)
                    part.pop()

        dfs(0)
        return ans

    # Create helper function, isPali, to determine if a string is a palidrome, 
    # Same word in reverse and normal
    # Function will take the string, left and right pointer
    # Use two pointer method to determine if left pointer == right pointer, go inward if s
    def isPali(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


