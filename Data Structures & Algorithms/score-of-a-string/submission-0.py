class Solution:
    def scoreOfString(self, s: str) -> int:
        # Brute Force approach: Iterate through each character in the string,
        # Convert each char into their ASCII values using ord() functino
        # Append values into an array or use array maninpulation
        # To get the abs value of difference between adjacent chars

        # Initialize arr that converts string into list that splits characters
        # Ans variable to holds score of each adjacent char
        arr = list(s)
        ans = 0
        
        # Iterate through the entire list, get score of current char with adjacent char
        for i in range(len(arr) - 1):
            ans += abs(ord(arr[i]) - ord(arr[i + 1]))
        return ans
            

