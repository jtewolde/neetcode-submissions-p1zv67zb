class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Approach Use a greedy method to use the given pairs to determine how long a pair chain can be formed
        # Two pairs are chained when the right endpoint is less than the left endpoint of the next pair
        # Example: [-2, 0] -> [1, 3] is a chain since 0 < 1 

        # Sort the pairs array based on the right endpoint of each pair
        # Initialize chainLen to keep track of the current chain length and end for tracking current right endpoint value
        pairs.sort(key=lambda p: p[1])
        chainLen = 1
        end = pairs[0][1]

        # Iterate through each pair in pairs array except for the first pair
        for indx in range(1, len(pairs)):
            # See if endpoint is less than start point of curr indx can be chained
            if end < pairs[indx][0]:
                # Increment chainLen by one and update end variable with next pair endpoint
                chainLen += 1
                end = pairs[indx][1]
        return chainLen