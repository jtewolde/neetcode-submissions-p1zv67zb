class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # Approach: Use iteration/Greedy to build out the new maximum odd binary number
        # First, create two counters, one for counting number of 1's and number of 0's in s string
        # Use counters for both 1 and 0 to determine how to build out new binary number that is valid
        # First, we want all of the 1's except one to be at the front of binary number to get the max number created
        # Then, add all of the zero's in the middle
        # Finally, add the last one in the end to make sure that the binary number is odd

        # Initialize counters for counting both 1's and 0's in binary number
        ones, zeros = 0, 0

        # Traverse through the binary string, count ones and zeros for constructing max binary number
        for num in s:
            if num == '1':
                ones += 1
            else:
                zeros += 1

        # Construct max binary number where you put all but one 1's in the beginning
        # Then, put all of the zeros in the middle,
        # Finally, put htelast 1 to make the max binary number odd
        maxBinaryNum = (ones - 1 ) * '1' + (zeros) * '0' + '1'

        return maxBinaryNum