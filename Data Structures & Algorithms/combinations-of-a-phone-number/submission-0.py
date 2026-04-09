class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Approach to solving this digits problem with Backtracking
        # First, use a hash map to map out digits to associated characters
        # Example: '2':'abc' ...
        # Create a ans variable for final answer
        # Initialize a backtrack function where it has two arguments, 
        # index for tracking curr index, and curStr to keep track of current string
        # Create base case for if the len(curStr) == len(digits), then append curStr to ans and return as string is created
        # Then, create for loop that goes through every character mapped to the hashmap
        # Call backtrack function with index + 1 and adding current char to charSum
        # Outside of function, call backtrack function with 0 index and empty string if there are digits
        # Return ans

        ans = []
        digitToChars = {
            "2": "abc",
            '3': 'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        def backtrack(indx, curString):
            if len(curString) == len(digits):
                ans.append(curString)
                return

            for char in digitToChars[digits[indx]]:
                backtrack(indx + 1, curString + char)

        if digits:
            backtrack(0, "")

        return ans




