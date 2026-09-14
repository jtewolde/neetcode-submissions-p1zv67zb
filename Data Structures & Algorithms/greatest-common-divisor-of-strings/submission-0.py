class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Approach: Use a greedy approach to fidn the GCD by adding both strings in either order
        # If the two strings concatenated together in either order produces the same result, it means it has the same repeating pattern.
        # Once verified both have the same pattern of chars, use built-in funciton GCD to get the common divisor between the two

        # Check if the concatenation of both strings in either order are the same, 
        # If not then return empty string
        if str1 + str2 != str2 + str1:
            return ""

        # Use the built-in GCD function to find the length of the largest common divisor between strings
        # Return the prefix using cd
        cd = math.gcd(len(str1), len(str2))
        return str1[:cd]
