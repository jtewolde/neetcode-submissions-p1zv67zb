class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Brute Force Approach: Create a row variable that counts the number of complete rows.
        # Create a while loop that executes when the number of coins is less than number of ompleted rows
        # Increment row by one and decrement n variable by one

        row = 0

        while n - row > 0:
            row += 1
            n -= row
        return row