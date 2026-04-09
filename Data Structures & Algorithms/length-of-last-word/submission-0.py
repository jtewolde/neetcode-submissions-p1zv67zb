class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Logic: Split the orignal string into multiple parts by splitting with spaces
        # Count the length of the last word from split string and return its length as answer
        
        # Initialize words array that takes the split string and turns them into words each index
        words = s.split()

        return len(words[-1])
        