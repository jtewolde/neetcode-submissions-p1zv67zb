class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Approach to solving this problem is by using Greedy
        # Synopsis: Sort the intervals array by the start vals
        # Iterate through the entire intervals array
        # Keep track of previous interval's end val, first setting it to the first interval's end val
        # Compare prevEnd to the start of next interval's,
        # If prevEnd >= start of next interval, it is overlapping
        # Set prevEnd to the minimum of prevEnd and current interval's end
        # Increment counter varaible to be returned at end

        # Create counter variable to keep track of intervals being removed
        counter = 0
        # Sort intervals array by starting vals
        intervals.sort(key = lambda interval: interval[0])
        # Initialize prevEnd variable with first interval's end value
        prevEnd = intervals[0][1]

        # Iterate through interval array starting from first interval,
        # Take the start and end val from current interval
        for startVal, endVal in intervals[1:]:
            # If start val of current interval is >= end of previous interval, there is no overlapping
            # Just set prevEnd to current interval's end val and go to next interval
            if startVal >= prevEnd:
                prevEnd = endVal
            # Otherwise, there is overlapping
            else:
                # Incrememt counter by one since there is overlapping
                # Set prevEnd to be the minimum between current val of prevEnd and end value of current interval
                counter += 1
                prevEnd = min(prevEnd, endVal)

        return counter




        
