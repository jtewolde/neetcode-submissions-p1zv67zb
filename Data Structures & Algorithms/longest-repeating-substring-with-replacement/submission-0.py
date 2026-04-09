class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Approach for solving this sliding window problem is similar to previous problem
        # Synopsis: Initialize a dictionary where it stores letters in string and its count
        # Left pointer starts at 0 while right pointer will increase, iterating through each char in string
        # Longest answer variable to track the longest substring with one distinct char
        # Create a for loop that increases right pointer for each char, increasing window
        # Add the current char on right pointer to hashmap,
        # For every potential window, there are a number of replacments to make window valid
        # In order to find out, see if the difference between current window size and the max frequency of a letter is less than or equal to value of k
        # If there isn't enough k replacements for window and characters, shrink window by moving left up 1
        

        longest = 0 # Store length of longest substring
        count = {} # Set to store letters as keys and their counts as values
        left = 0 # Left pointer of window
        max_freq = 0 # Stores the maximum frequency of a character inside of current window

        # Expand the window size by having right pointer start at 0 and go through entire string lengh
        for right in range(len(s)):

            # Increase the frequency of current letter in string by one
            count[s[right]] = count.get(s[right], 0) +  1

            # Set the max frequency of letters in window by comparing count of current letter to previous max
            max_freq = max(count[s[right]], max_freq)

            # If there isn't enough k replacments for the current window size and the max freq of character in window
            while (right - left + 1) - max_freq > k:
                # Decrement count of letter on left pointer and move left pointer up one to shrink window
                count[s[left]] -= 1
                left += 1

            # Update longest substring length by comparing to current val and the current window size
            longest = max(longest, (right - left + 1))

        return longest
