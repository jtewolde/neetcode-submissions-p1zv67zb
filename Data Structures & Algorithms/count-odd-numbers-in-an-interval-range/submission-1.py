class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Optimal Approach: Use Math to get the range of numbers between low and high parameters
        # Then, use modular division to count how many odd numbers there are within the range
        # Also, check the starting number, low, is also odd. If so, increment the count by 1 and return it

        # Initialize length and oddCount variables where length stores the range
        # OddCount stores the result of modular division between length // 2
        length = high - low + 1
        oddCount = length // 2

        if length % 2 and low % 2:
            oddCount +=1 
        return oddCount