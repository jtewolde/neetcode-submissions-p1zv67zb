class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Approach: Use hashmaps/Counters to count the frequencies of each letter in ransomNote magazine string
        # Compare the frequencies of each character in ransomNote and see if each count is equal or greater than in magazine
        # If count of char in magazine is less than count of char in ransom, return False
        # Else, return True

        # Initialize counters for each string to count the frequencies of each char in both strings
        countRansom = Counter(ransomNote)
        countMag = Counter(magazine)

        # Iterate through each character that was counted in ransomNote
        for char in countRansom:
            # See if count of current char in magazine string is less than count in ransom. return false
            if countMag[char] < countRansom[char]:
                return False
            # Otherwise, continue with the 
            else:
                continue

        return True