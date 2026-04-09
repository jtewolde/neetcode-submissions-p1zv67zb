class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort both strings using sorted function
        # Compare both sorted strings
        # If both are equal to each other, return true, else false

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s == sorted_t:
            return True
        else:
            return False
        