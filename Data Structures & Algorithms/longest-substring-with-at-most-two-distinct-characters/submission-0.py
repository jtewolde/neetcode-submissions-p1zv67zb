class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # Approach: Use sliding window method to find max substring with two distinct characters
        # Initlialize two pointers, l and r, on index 0 and 1 to iterate through string.
        # Create max_length variable to keep track of length of longest substring with at most two distnct characters
        # For current window, keep track of number of distinct chars either using Counter or counting diff chars
        # If window's distinct chars > 2, move left pointer forward to shrink window and get new char

        # Initialize left pointer, max_length, and cnt to track freqs of chars in window
        cnt = Counter() 
        left = 0
        max_length = 0
        n = len(s)

        # Traverse through the string by incrementing right pointer until end of string
        for right in range(n):
            cnt[s[right]] += 1 # Add current char into the counter map

            # While the cnt map has more than 2 distinct chars
            while len(cnt) > 2:
                cnt[s[left]] -= 1 # Decrease count of leftmost character in window\

                # If the count of character is zero, remove it from the cnt map
                if cnt[s[left]] == 0:
                    del cnt[s[left]]   

                left += 1 # Increment left pointer inward

            # Update max_length of substring with current window size
            max_length = max(max_length, right - left + 1)

        return max_length


            