class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Approach: Use hashmaps and iteration to compare chars in words 
        # To see if they are in order based on alien language
        # In theory, the chars in words[2] should be greater than chars in words[1
        # First, initialize hashmap that maps every char in order string to index position
        # Then, iterate through both adjacent words in words array
        # Simply, iterate and compare chars ata each position until difference is found or one word ends
        # If words[1] is longer than words[2] and all chars compared are the same, then return False
        # If any characters differ, check if index of words[1] char < index of words[2] char using order hashmap
        # If not, return False. Otherwise, return true as default

        # First, initialize hashmap that maps every char in order string to index position
        order_map = {char: idx for idx, char in enumerate(order)}

        # Then, iterate through both adjacent words in words array
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            # If words[1] is longer than words[2] 
            # and all chars compared are the same, then return False
            for j in range(len(word1)):
                if j == len(word2):
                    return False

                # If any characters differ, 
                # Check if index of words[1] char > index of words[2] char using order hashmap
                # If true, then return False. Otherwise, break from for loop
                if word1[j] != word2[j]:
                    if order_map[word1[j]] > order_map[word2[j]]:
                        return False
                    break

        return True



