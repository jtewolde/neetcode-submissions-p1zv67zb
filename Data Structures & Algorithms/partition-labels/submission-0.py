class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Approach for solving this problem is to using Two Pointers and Greedy Techinques
        # Synopsis: Iterate through the string to get the sizes of paritions and add them to the final anrray
        # Create hashmap to map out characters to the last index they appear in string
        # Then, initialize variables, size for size of partition, end for end of parition, and ans for storing sizes
        # Iterate/enumerate through string, increment size for every char visited 
        # Update end of parition by getting the max between itself and last index of current char
        # Then, if the index of current char == end of parition,
        # Append current size to the ans array and reset size to 0 for new parition

        # Create hashmap to map out chars to their last indexes,
        # Also, create ans variable to store sizes of paritions
        lastIndex = {}
        ans = []

        # Initialize size and end variables to 0
        size, end = 0, 0

        # Iterate/Enumerate through string, map out chars to indexes
        for ind, char in enumerate(s):
            lastIndex[char] = ind

        # Iterate through string with ind and char,
        # For every char, 
        # Increment size up 1 and update end variable to max between itself and current char's last index
        for ind, char in enumerate(s):
            size += 1
            end = max(end, lastIndex[char])

            # If current index of char is equal to the end of parition
            # Append size to ans array and reset size back to zero for new parition
            if ind == end:
                ans.append(size)
                size = 0

        return ans


        

