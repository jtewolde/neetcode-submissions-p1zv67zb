class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initial approach using Sliding Window Strategy
        # Create a hashset to keep track of characters with no duplicates
        # Create ans variable to keep track of max length of the substring 
        # Initialize left and right pointers, with left = 0 and right being changed throughout loop
        # Create for loop where the right pointer changes throughout
        # While the char on right pointer is a duplicate, remove the left char from the set and move left up one
        # If right char is not duplicate, add char to the set
        # Update ans to new length of substring between current length and max of new length
        # Return ans as final answer

        # create set and left pointer
        charSet = set()
        left = 0
        ans = 0

        for right in range(len(s)):
            # while character on right pointer is in the set, meaning its a duplicate
            while s[right] in charSet:
                # Remove character in left pointer to move sliding window
                # Move left pointer to the right by one to move sliding window
                charSet.remove(s[left])
                left += 1
            # Add new character on right pointer to set
            charSet.add(s[right])
            # Update current length of substring to new length if greater
            ans = max(ans, right - left + 1)
        return ans