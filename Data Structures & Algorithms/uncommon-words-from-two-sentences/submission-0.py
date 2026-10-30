class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Approach: Use a hashmap/Counter to count the each word in each string 1 and 2.
        # Iterate through each string and count the words using string concateration
        # Then, create an ans array to stroe the words that only have a count of 1 and return the array

        # Initialize count hashmap to store the count of each word in strings
        # Also, create ans array that will store the uncommon words in both strings
        count = defaultdict(int)
        ans = []

        # Iterate through the combined strings using each word
        for word in s1.split(" ") + s2.split(" "):
            count[word] += 1
        
        # Iterate through each word in the count hashmap
        for word, cnt in count.items():
            # If the count of the curr word is one, then add to ans array as it is uncommon
            if cnt == 1:
                ans.append(word)
        return ans
