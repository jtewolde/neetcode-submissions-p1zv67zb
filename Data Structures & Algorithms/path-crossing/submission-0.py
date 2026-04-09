class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Approach: Use a hash set data structure to keep track of the visited coordinates depending on direction
        # First, initialize hashset, visited, to store visited coordinates after going a direction
        # Add the origin/starting point of in visited being (0,0) by creating x and y to be both 0
        # Also, create directions hashmap that stores the different directions that could be taken depending on letter in the path

        # Create directions hashmap that stores the different directions 
        # that could be taken depending on letter in the path
        directions = {
            'N': [0 , 1],
            'S': [0, -1],
            'E': [-1, 0],
            'W': [1, 0]
        }

        # First, initialize hashset, visited, to store visited coordinates after going a direction
        # Add the origin/starting point of in visited being (0,0) by creating x and y to be both 0
        visited = set()
        x, y = 0, 0

        # Iterate through each character in the path string, add current coordinate to visited for origin
        for char in path:
            visited.add((x,y))
            # Update x and y variable based on directions from char using dx and dy
            dx, dy = directions[char] 
            x, y = x + dx, y + dy

            # IF the current x-y coordinates are in visited set, then return True
            if (x, y) in visited:
                return True
        return False

