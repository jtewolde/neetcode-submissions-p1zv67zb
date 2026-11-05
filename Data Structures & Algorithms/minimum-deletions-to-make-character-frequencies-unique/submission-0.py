class Solution:
    def minDeletions(self, s: str) -> int:
        # Approach: Use a Counter hashmap to count all of the characters in the given string to get frequencies
        # Then, iterate through the counter hashmap and determine if the current char frequency is already used
        # If so, then decrement the frequency of that char and increment ans variable that will keep track of deletions
        # Otherwise, add the frequency into the used freq hashset

        # Initialize counter for getting frequencies of chars in string, 
        # Used_freq hashset for storing freqs that had been used. Also, ans variable for tracking num of deletions
        count = Counter(s)
        used_freq = set()
        ans = 0

        # Iterate through each char and its freq in the counter hashset
        for char, freq in count.items():
            # Make sure the freq of the current char is greater than 0 and if the freq is already used
            while freq > 0 and freq in used_freq:
                # Decrement freq of this current char and increment ans by one for deletion
                freq -= 1
                ans += 1
            used_freq.add(freq)
        return ans