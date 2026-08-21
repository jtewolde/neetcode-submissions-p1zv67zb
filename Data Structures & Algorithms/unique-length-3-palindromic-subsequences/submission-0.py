class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Approach: Use hashsets and iteration to find at least two occurrences of current character to form a valid palindrome of length 3
        # A palindrome is valid f te firs and last index are the same character with mid character being any char
        
        # Create ans variable to keep track of number of distinct characters in between
        ans = 0

        # First, iterate through every character in alphabet, from "a" to "z"
        for charIndx in range(26):
            # Get the current character to check if it is in string
            char = chr(ord('a') + charIndx)

            # Find the first and last char index of current char that appears in the string
            # If the current character doesn't appear twice in string, then skip the character
            left, right = s.find(char), s.rfind(char)
            if left == -1 or left == right:
                continue

            # Create a hashset that stores the middle distinct characters between indices of left + 1 and right
            mids = set()
            # Iterate through each indx of character between left and right chars in palindrome
            # Add each distinct character to the set
            for midIndx in range(left + 1, right):
                mids.add(s[midIndx])
            # Increment ans with the length of mids set
            ans += len(mids)

        return ans
