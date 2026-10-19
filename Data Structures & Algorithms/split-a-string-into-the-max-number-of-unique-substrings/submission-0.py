class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # Approach: Use backtracking and hashsets to iterate through given string and form max unique substrings

        # Initialize used hashset to store substrings that already been used
        used = set()

        # Create DFS search function which takes start index as parameter
        def search(start):
            # If all of the characters have been processed, then return 0
            if start == len(s):
                return 0

            # Tracks the best number of substrings for this current path
            best = -len(s)

            # Try every possible substring starting at 'start' index
            for end in range(start + 1, len(s) + 1):
                piece = s[start:end]
                
                # If the current substring hasn't been used, then add to used hashset
                if piece not in used:
                    used.add(piece)
                    # Count the substring and solve the remaining string
                    # Also, backtrack by removing the substring so other substrings can use it
                    best = max(best, 1 + search(end))
                    used.remove(piece)
            return best
        return search(0)

