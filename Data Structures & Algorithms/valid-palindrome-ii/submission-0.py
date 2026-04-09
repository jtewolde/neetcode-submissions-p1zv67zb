class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Use Two Pointers approach to solve this problem similar to Valid Palindrome 1
        # Can delete one character that doesn't make string valid
        # Logic: If the chars at each pointer aren't equal, to decide which char is removed
        # Use both situations where skipping chars at each pointer
        # Reverse each substring with skipping each pointer to see if it is still a palindrome or not

        # Initialize two pointers, left and right
        left = 0
        right = len(s) - 1

        # Go through string with two pointers
        while left < right:
            # If the characters at each pointers aren't equal, it is not a palindrome
            if s[left] != s[right]:
                # Initialize two substrings of s for each scenario, one for deleting/skipping the left char
                # Another for deleting/skipping the right character
                delLeft = s[left + 1 : right +  1]
                delRight = s[left : right]
                
                # See by deleting either character makes the string back to a valid palindrome
                return(delLeft == delLeft[::-1] or delRight == delRight[::-1])

            # Move inward to other characters
            left += 1
            right -= 1

        return True

