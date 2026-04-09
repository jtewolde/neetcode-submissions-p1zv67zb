# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Logic: Use Binary Search to find the number that was picked by dividing and conquer
        # Use the pre-defined guess API to determine if number is higher/lower/equal
        # With Binary Search: Create low and high variables that equals 1 and n
        # Create middle val where low + high // 2.
        # Use middle val with guess function to determine if mid is higher/lower/equal to picked num

        # Initialize low and high pointers that start from 1 and n values
        low = 1
        high = n

        # Loop through all numbers from 1 to n
        while low <= high:
            # Create mid value for the pivot
            mid = (low + high) // 2

            # Case 1: If middle val is equal to picked
            if guess(mid) == 0:
                return mid
            # Case 2: If middle val is greater than pick
            # Search lower half of values
            elif guess(mid) == -1:
                high = mid - 1
            # Case 3: If middle val is less than pick
            # Search upper half of values
            elif guess(mid) == 1:
                low = mid + 1

        return mid

