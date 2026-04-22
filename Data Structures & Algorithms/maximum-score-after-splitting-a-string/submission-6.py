class Solution:
    def maxScore(self, s: str) -> int:
        # Approach: Use iteration to count the number of zeros and ones in string
        # Initialize zero variable that will store the count of zeros through iteration and ans variable
        # Create ones variable that will hold the count of ones immediately using count method
        # Iterate through string with using for loop
        # Determine if current num is zero or one, if zero -> increment zero variable by one
        # Otherwise, decrement total count of ones variable 
        # Then, update ans variable by taking maximum between itself and sum of ones and zeros

        # Initialize zero variable that will store the count of zeros through iteration and ans variable
        # Create ones variable that will hold the count of ones immediately using count method
        zeros = 0
        ones = s.count('1')
        ans = 0

        # Iterate through string with using for loop
        for i in range(len(s) - 1):
            # Determine if current num is zero or one, 
            # if zero -> increment zero variable by one
            if s[i] == '0':
                zeros += 1
            # Otherwise, decrement total count of ones variable 
            else:
                ones -= 1
            # Update ans variable by taking maximum between itself and sum of ones and zeros
            ans = max(ans, zeros + ones)
        return ans


