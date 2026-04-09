class Solution:
    def isPalindrome(self, s: str) -> bool:
    # Pseudocode for initial approach: Two Pointers
    # 1. Initialize left and right variables for pointers with left = 0 and right = len(s) - 1
    # 2. Start from start and end of string
    # 3. If either the pointers are white spaces, or not letters, skip letter
    # 5. IF two letters are the same letter, move both towards center
    # Else, return false

        left = 0;
        right = len(s) - 1;

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() == s[right].lower(): 
                left += 1
                right -= 1
            else:
                return False
        return True


