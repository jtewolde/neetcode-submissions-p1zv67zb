class Solution:
    def isHappy(self, n: int) -> bool:
        # Problem: Determine if the given number is happy by taking the sum of squares of each digit in the number repeatedly
        # The number is happy if the cycle eventually reaches 1. Return true if it does and false if it falls into a cycle
        # Approach: Use fast and slow pointers used on linked list problems to detect cycles after each transformation

        # Initialize slow pointer with given n value and fast pointer as the result of the sum of squares function with n
        slow = n
        fast = self.sumOfSquares(n)

        # Create while loop for slow and fast pointers where the slow pointer moves one step and the fast pointer moves two steps
        while slow != fast:
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)
        # When the loop ends, determine if a cycle has been detected if the fast pointer reaches a 1, return True
        # Otherwise, return False as it reaches a cycle
        return True if fast == 1 else False

    # Helper function to get the sum of squares for each digit with the given number in parameter
    def sumOfSquares(self, n: int) -> int:
        result = 0

        # Get each digit from the given num, square it, and then add to the result variable that holds the entire sum
        while n:
            digit = n % 10
            digit = digit ** 2
            result += digit
            n = n // 10
        return result
