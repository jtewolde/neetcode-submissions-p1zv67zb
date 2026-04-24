class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Approach: Use counter to count the frequency of each character in the string
        # Find if there is a character that has a count of exactly one to be unique, return the index of that character
        # First, initialize Counter variable for the freq of characters
        # Then, iterate through the characters in s using index and range
        # Get the current character in for loop iteration
        # Determine if current char has count of exactly one

        # First, initialize Counter variable for the freq of characters
        count = Counter(s)

        # Then, iterate through the characters in s using index and range
        for indx in range(len(s)):
            # Get the current character in for loop
            currChar = s[indx]
            # Determine if current char has count of exactly one
            # If true, return the index of the unique character
            if count[currChar] == 1:
                return indx
        return -1