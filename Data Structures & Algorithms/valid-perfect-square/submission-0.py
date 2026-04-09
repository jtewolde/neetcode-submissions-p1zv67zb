class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Approach: Use binary search to find the perfect square integer
        # Initialize low and high pointers where low = 1 and high = num to loop through range of numbers
        # Loop through range of nums between low and high
        # Create midpoint variable that tracks middle of range of nums to find perfect square
        # Compute actual square of num with current midpoint:
        # If current square with mid is less than num: set high to midpoint - 1
        # If current square with mid is greater than num: set low to midpoint + 1
        # If current squared with mid equals num, return true value, otherwise return false as default

        low, high = 1, num

        while low <= high:
            midpoint = (low + high) // 2
            squared = midpoint * midpoint

            if squared < num:
                low = midpoint + 1
            elif squared > num:
                high = midpoint - 1
            else:
                return True

        return False
