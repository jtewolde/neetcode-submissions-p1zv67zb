class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Approach for solving this problem is with using sliding window techinque

        # First, see if the length of string 1 is greater than length of string 2
        # Return false if s1 > s2
        # Initialize two arrays, s1Count and s2Count, which stores the count of each letter in string
        # Both arrays will be [0] * 26 where each letter in alphabet will have count of zero
        # Iterate through len of s1, update s1Count with the new counts of letters in s1
        # Use ord function to get the ASCII value of letter
        # Maintain a sliding window size of S1, update frequencies of letters in that window to s2
        # See if both arrays are equal to each other after going through s1, if so, return True
        # Else, continue by iterating through string s2 and moving the sliding window through s2
        # Add new characters to the s2Freq array with the right pointer's index using ord() function#
        # Increment that character's frequency by one
        # For the left pointer, decrease the frequency of left pointer's character from s2Freq
        # Then, compare both arrays, if they are equal, return True.
        # Else, move the window across s2
        # By default, return False

        s1Len = len(s1)
        s2Len = len(s2)

        # See if length of s1 > s2, 
        # if so, that means there are no permutations and return false
        if len(s1) > len(s2):
            return False

        # Initialize freq arrays for both strings, where each letter has freq/count of zero
        s1Freq = [0] * 26
        s2Freq = [0] * 26
        base = ord('a') # get the ASCII value of 'a'

        # Iterate through length of s1 string, update frequencies of letters in both strings in that window
        # Use ord() function to convert letters to ASCII values to make fixed value of 26 letters array
        for ind in range(len(s1)):
            s1Freq[ord(s1[ind]) - base] += 1
            s2Freq[ord(s2[ind]) - base] += 1

        # See if both dictionaries are equal after first update, return True
        if s1Freq == s2Freq:
            return True

        # Loop right pointer starting at length of s1 to end of string 2 length to expand window
        for right in range(s1Len, s2Len):
            s2Freq[ord(s2[right]) - base] += 1 # Add to count of letter on right pointer
            s2Freq[ord(s2[right - s1Len]) - base] -= 1 # Remove left character from s2Freq array

            # Compare both arrays, if they are the same, return True
            if s1Freq == s2Freq:
                return True

        return False



        




