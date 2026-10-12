class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Approach: Use prefix sums and a hashset to iterate through all words within the range of given query.
        # Determine if the current word is a vowel string if the starting and ending letter are vowels
        
        # Initialize needed variables like hashset with vowels, prefix sum array with size of n + 1, all initialized with 0
        # Also, create prev variable that will be used to set prefix count of index + 1
        vowel_set = set("aeiou")
        prefix_count = [0] * (len(words) + 1)
        prev = 0

        # Iterate through each word and its index from the words array
        for indx, word in enumerate(words):
            # Make sure the current word is a valid vowel string if first and last char are vowels
            # Increment prev variable by one and set prefix_count for indx + 1 to prev
            if word[0] in vowel_set and word[-1] in vowel_set:
                prev += 1
            prefix_count[indx + 1] = prev

        # Initialize ans array that stores the num of valid vowel strings for each query range
        # Iterate through queries array using current indx and query
        ans = [0] * len(queries)
        for indx, query in enumerate(queries):
            left, right = query
            ans[indx] = prefix_count[right + 1] - prefix_count[left]

        return ans

