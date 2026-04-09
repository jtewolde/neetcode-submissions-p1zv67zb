class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Logic: In this problem, you are finding the longest common prefix amongst strings
        # Prefix means the first letters in a word
        # Return the length of the longest common prefix in all words in strs

        # Brute force: Nested for loop where you would compare the letters in the first word in strs array
        # If the current letter at index for current string and first string are equal, then return ans string
        # Else, add letter to ans string for longest common prefix

        # Initialize ans string that will hold the longest common prefix amongst strs
        ans = ""

        # Iterate through each letter in first string to compare with other strings
        for indx in range(len(strs[0])):
            # Loop through every string in strings array
            for s in strs:
                # Check if common prefix can continue with string
                # See if index is out of bounds or letter of first letter doesn't match with current string at index
                # Return longest common prefix amongst strs array as it can't add more letters
                if indx == len(s) or s[indx] != strs[0][indx]:
                    return ans

            # Add next letter to common prefix from first string 
            ans += strs[0][indx]
            
        # Return longest common prefix 
        return ans