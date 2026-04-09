class Solution:
    # Approach to solve this problem is to use length of string as way to identify strings that need to be decoded
    # First, can't use a delimiter symbol like '#' or '.' as strings would not be correct
    # If there is already a # or . inside of original string
    # To Encode: Iterate through strs array and for each string in array,
    # Take the length of current string and append it with a delimiter like # before the actual string chars
    # Idea is that when decoding, it will use length of string char to identify how many chars after delimiter to get orignial string
    
    def encode(self, strs: List[str]) -> str:
        # Empty string for storing encoded full string
        ans = "" 

        # For each string in array, append the length of string and a delimiter before it
        # Append the combination to the ans string to make them together and be encoded
        for s in strs:
            ans += str(len(s)) + "#" + s
        return ans

    def decode(self, s: str) -> List[str]:
        # Initialize ans for empty array and indx for iterating through given string
        ans = [] 
        indx = 0

        # Go through entire string array, find the length of first string num 
        # When encountering delimiter char
        while indx < len(s):
            delimit = indx
            # If not encountering delimiter, move delimit pointer inward
            while s[delimit] != '#':
                delimit += 1
            # When encountering delimiter, get the length of string number before delimiter 
            len_of_string = int(s[indx:delimit])

            # Create variables that indicate more easily when the decoded string starts and ends
            start_of_str = delimit + 1
            end_of_str = start_of_str + len_of_string

            # Move indx variable to end of string to start decoding next string
            indx = end_of_str   

            ans.append(s[start_of_str : end_of_str])
        return ans
