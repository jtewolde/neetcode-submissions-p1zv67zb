class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Use Two Pointers approach to reverse string by swapping letters

        # Initialize left and right pointers to reverse string, starting from zero to end of string
        left = 0
        right = len(s) - 1

        # Iterate through string with two pointers
        while left < right:
            # Swap characters at each pointer
            s[left], s[right] = s[right], s[left]
            # Move inward in the string
            left += 1
            right -= 1
