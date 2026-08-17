class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # Approach: Use a hashmap to keep track of positions on brick wall where there is the most gaps between bricks.
        # The goal is to cut the least amount of bricks with a vertical line down the wall
        # Iterate through each row on the wall and count the brick widths except the last brick
        # Then, for each width, increment the gap's count in the hash map
        # Finally, find the maximum count in the hashmap which represents the most amount of gaps that are aligned
        # Return the difference between total # of rows and the max aligned gaps

        # Initialize countGaps hashmap that counts the number of aligned gaps on each position
        countGaps = { 0 : 0 }

        # Iterate through each row on the wall and set the total number of gaps to zero
        for row in wall:
            currGaps = 0
            # Then, for each width, increment the gap's count in the hash map
            for brick in row[:-1]:
                currGaps += brick
                countGaps[currGaps] = 1 + countGaps.get(currGaps, 0)
        # Return the difference between total # of rows and the max aligned gaps
        return len(wall) - max(countGaps.values())
