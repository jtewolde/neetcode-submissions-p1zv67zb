class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # First approach: Use frequency counting with Counters to count all available characters in chars
        # Initialize ans variable that stores sum of lenght of all good strings in words
        # Then, count the chars in each word in the words array
        # Compare the count of chars of each word to chars string
        # If the character requirements are met, then consider word to be a good string
        # Add length fo good string in words to ans

        # Initialize ans variable that stores sum of lenght of all good strings in words
        # Also, initialize counter for chars string 
        ans = 0
        count = Counter(chars)
        
        # Iterate through every word in the words array
        # Use counter to count the characters in each word
        for word in words:
            word_count = Counter(word)

            # Iterate through all characters in word_count
            # And compare the frequency of that char in count to word_count
            # If the freq of char in count is greater or equal to freq of current word in words
            # Increment len of current word to ans variable
            if all(count[char] >= freq for char, freq in word_count.items()):
                ans += len(word)

        return ans
