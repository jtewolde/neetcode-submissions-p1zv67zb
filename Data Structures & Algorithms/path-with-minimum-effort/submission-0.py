class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Approach: Use Dijkstra's algorithm which uses BFS and a minheap to keep track and find the path has the minimum effort
        # Goal is to find a path in the heights array that has the lowest absolute difference between consective heights to the bottom right element
        
        # First, initialize needed variables and data structures for BFS like minHeap for tracking path
        # Visited hashset to store all previously visited heights
        # Then, directions array that stores the possible directions that can be taken when finding optimal path
        # Also, store the entire dimension of heights array in ROWS and COLS
        minHeap = [[0, 0, 0]] # [diff, row, col]
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(heights), len(heights[0])

        # Iterate through all of the paths in the minHeap currently while it isn't empty
        while minHeap:
            # Pop out the most recent cell from minHeap and its difference with its current position
            diff, row, col = heapq.heappop(minHeap)

            # Check if curernt position has been visited, if true then continue with next iteration of loop
            # Otherwise, add the cell into the visited
            if (row, col) in visited:
                continue
            visited.add((row, col))

            # Also, check if the current cell is the final destination, which means return the current diff
            if (row, col) == (ROWS -1, COLS - 1):
                return diff

            # Loop through each of the four directions and make sure that the new row and col are valid and within boundaries
            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc
                if ( newRow < 0 or newCol < 0 or newRow >= ROWS or newCol >= COLS or (newRow, newCol) in visited):
                    continue

                # Calculate the new difference by finding the max between the current diff and the absolute height difference
                # Push the new difference and the new cell position into the heap
                newDiff = max(diff, abs(heights[row][col] - heights[newRow][newCol]))
                heapq.heappush(minHeap, [newDiff, newRow, newCol])
        return 0





