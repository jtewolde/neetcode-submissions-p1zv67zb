class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Approach: Use sliding window approach to determine what 'W's to recolor to 'B' for K consective 'B' Blocks
        # Initialize ans variable that stores minimum recolors and count for storing count of white blocks in current window
        # First, count the number of 'W' chars in current first window(left to right) and store in count variable
        # Create for loop starting from index k to end of the blocks string
        # If the oncoming char from right side at index i(blocks[i]) is 'W', then increment count by 1
        # If the leaving char from left at index i - k is 'W', then decrement count by 1
        # Update ans with minimum recolors from count and current val of anas

        # Initialize count for storing count of white blocks in current window
        count_WBlocks = 0

        # First, count the number of 'W' chars in current first window(left to right) 
        # And store in count variable
        for i in range(k):
            if blocks[i] == 'W':
                count_WBlocks += 1

        # Initialize ans variable that stores minimum recolors
        ans = count_WBlocks

        # Create for loop starting from index k to end of the blocks string
        for i in range(k , len(blocks)):
            # If the oncoming char from right side at index i(blocks[i]) is 'W', then increment count by 1
            if blocks[i] == 'W':
                count_WBlocks += 1
            # If the leaving char from left at index i - k is 'W', then decrement count by 1
            if blocks[i - k] == 'W':
                count_WBlocks -= 1

            ans = min(ans, count_WBlocks)

        return ans
