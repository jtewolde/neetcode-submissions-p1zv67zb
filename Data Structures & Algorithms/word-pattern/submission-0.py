class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Approach: Map each letter in string with a word in pattern string
        # Split the string into words and see if length of splitted string equals len of pattern
        # First, create two dictionaries for bidirectional mapping, 
        # One for mapping word to letter, other for mapping letter to word
        # Iterate through both strings at the same time
        # Compare letter in s and word in pattern at same index to see if they are mapped the same

        # Split the string into words and see if length of splitted string equals len of pattern
        words = s.split()
        if(len(words) != len(pattern)):
            return False
        
        # Initialize both dictionaries for bidirectional mapping
        wordCharMap = {} # Mapping word from pattern to char from s
        charWordMap = {} # Mapping char from s to word from pattern

        # Iterate through both strings at the same time using zip
        for word, char in zip(words, pattern):
            # Make sure that the bidirectional mapping between two hash maps are valid
            # If the mapping of word to char isn't valid, return false
            if char in charWordMap and charWordMap[char] != word:
                return False
            if word in wordCharMap and wordCharMap[word] != char:
                return False

            # If other chars are mapped correctly, then map current chars to each other
            wordCharMap[word] = char
            charWordMap[char] = word

        return True 

            
