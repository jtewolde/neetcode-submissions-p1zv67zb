class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Approach: Use one pointer to keep track of character in each string
        # Append each string's char into the ans string alternatively
        # If there are no chars in one string, just append the rest to the ans

        # Initialize variables for getting length of each word
        # Create ans string for final string
        str1 = len(word1)
        str2 = len(word2)
        ans = ""

        # Get the max length between both words for alternating strings
        maxLen = max(len(word1), len(word2))

        # Use maxLen to iterate through all chars in both strings
        for indx in range(maxLen):

            # Alternatively add chars in each word to ans string
            # If current index is less than length of word, add to string
            if indx < str1:
                ans += word1[indx]

            if indx < str2:
                ans += word2[indx]
            
        return ans
