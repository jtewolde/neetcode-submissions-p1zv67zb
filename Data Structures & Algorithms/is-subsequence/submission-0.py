class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Approach: Use two pointers to track the order and position of chars in s and t
        # Iterate through both strings at the same time
        # If both chars in both strings at the same index are equal, move the s pointer forward
        # Otherwise, just move the t pointer forward to the next index regardless

        # Initialize pointers for both strings
        s_pointer, t_pointer = 0, 0

        # Iterate through both strings at the same time
        while s_pointer < len(s) and t_pointer < len(t):
            # If the same character appears in both strings in relative positions,
            # Move s_pointer forward
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1

            # Otherwise, move t pointer regardless
            t_pointer += 1

        # If the value of s_pointer is the same as the length of the string,
        # Then, all chars in s are a subsequence of t string, return True
        return s_pointer == len(s)
