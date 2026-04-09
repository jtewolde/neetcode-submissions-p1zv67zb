class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # Approach: Use Iteration to find the maximum 3-same-digit number in the num string
        # Logic: Create an ans string variable to place the max substring and to be returned as final answer
        # Create a for loop for iterating through num string
        # Check if characters at indx, indx +1, and indx + 2 are the same character
        # If so, update the max substring to the ans variable
        
        # Initialize ans string variable to put max substring
        ans = ""
        
        # Iterate through entire num string except for last two characters since it doesn't fit
        for indx in range(len(num) - 2):

            # See if next three characters are the same as a substring
            if num[indx] == num[indx + 1] == num[indx + 2]:
                # Update ans with max substring  that is in num
                ans = max(ans, num[indx: indx + 3])
        # If there are no same 3 digit substring in num, then return empty string as ans doesn't change
        # Otherwise, return substring in ans
        return "" if ans =="0" else ans
