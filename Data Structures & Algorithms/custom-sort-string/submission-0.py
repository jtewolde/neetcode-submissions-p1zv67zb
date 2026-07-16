class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Use a frequency count strategy to build the final result string directly by counting char freqs
        # First, create a freq array of size 26 to count the occurances of each char in s
        # Iterate through each char in order string and for each char
        # Append it to the result string as many times as its count and set the count of char to zero
        # Then, deal with the rest of the characters by iterating through all 26 letters 
        # Append the remaining characters to the result based on their counts

        # First, create a freq array of size 26 to count the occurances of each char in s
        # Also, initialize ans array that will store new s string based on order string structure
        # Fill the freq array with the occurances of each character 
        countFreq = [0] * 26
        ans = []
        for char in s:
            countFreq[ord(char) - ord('a')] += 1

        # Iterate through every char in order string and calculate the index of each char for countFreq array
        for char in order:
            indx = ord(char) - ord('a')
            # For every char in order, append the current char to ans array as many times as its freq
            # Then, set the count of current char to zero
            while countFreq[indx]:
                ans.append(char)
                countFreq[indx] -= 1

        # Now, deal with the remaining characters not in order string by iterating through all 26 characters
        for indx in range(26):
            # Get the associated char with the index 
            # Append the remaining characters onto the end of the ans array and decrementing the char count
            char = chr(ord('a') + indx)
            while countFreq[indx]:
                countFreq[indx] -= 1
                ans.append(char)

        return ''.join(ans)
