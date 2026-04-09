class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Initial approach using Hash set:
        
        # Create a hashset to keep track of frequency of characters
        # Iterate through 's', if the character is not in the set, set freq to 1
        # Else, add one to the freq of the character

        # Then, iterate through the 't' string,
        # If the current character is not in the string, return False b/c it is not a valid anagram
        # If the current character is in the string, subtract the freq of character by 1
        
        # Return true if the freq of all characters in the set is zero

        character_freq = {}

        # if the two strings don't have same length, return false
        if len(s) != len(t):
            return False

        for char in s:
            if char not in character_freq:
                character_freq[char] = 1
            else:
                character_freq[char] += 1

        for char in t:
            if char not in character_freq:
                return False
            elif character_freq[char] > 0:
                character_freq[char] -= 1
            else:
                return False

        for key in character_freq:
            if character_freq[key] != 0:
                return False
        
        return True







