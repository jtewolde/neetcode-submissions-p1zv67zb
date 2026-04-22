class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # Synposis: Make all strings in owrds array equal to each other 
        # by moving any additional chars to a string that needs it
        # Approach: Use hashmaps to count the frequency of chars for each word
        # Initialize hashmap dictionary to get the frequency of chars in every word in array
        # Create nested for loop for iterating through every char in every word in array
        # Increment the count for the current char in hashmap
        # After getting the frequency of each char, 
        # Iterate through every char to see if the frequency is divisible by number of words
        # If not divisible evenly, return false as strings can't be equal
        # Otherwise, return True

        # Initialize hashmap dictionary to get the frequency of chars in every word in array
        chars_count = defaultdict(int)

        # Create nested for loop for iterating through every char in every word in array
        # Increment the count for the current char in hashmap
        for word in words:
            for char in word:
                chars_count[char] += 1

        # Iterate through every char to see if the frequency is divisible by number of words
        # If not divisible evenly, return false as strings can't be equal
        for freq in chars_count:
            if chars_count[freq] % len(words):
                return False
        
        return True


