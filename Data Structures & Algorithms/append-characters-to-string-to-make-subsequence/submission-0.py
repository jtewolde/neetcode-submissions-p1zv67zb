class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # Approach: Use two pointers method to iterate through both strings,
        # Initialize two pointer variables for traversing through s and t at the same time
        # Match/count characters that appear on both strings and move inward
        # If they don't match, ony move the pointer for s
        # After traversing through both strings, the value of the t string's pointer represent the amount of chars that already exist in s
        # The difference between the length of t string and pointer returns the number of chars to be appended

        # Initialize pointers for traversing both strings simultaneously
        sPoint = tPoint = 0

        # Iterate through both strings at the same time
        while sPoint < len(s) and tPoint < len(t):
            # Case 1: If both characters at pointers are equal, move both pointers to right
            if s[sPoint] == t[tPoint]:
                sPoint += 1
                tPoint += 1
            # Case 2: Don't match, only move pointer variable for s
            else:
                sPoint += 1

        # Return the difference between the length of t string and pointer returns the number of chars to be appended
        return len(t) - tPoint