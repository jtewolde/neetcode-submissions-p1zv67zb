class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Approach to solving this Intervals problem is using Greedy
        # Synopsis: Iterate through the intervals array, see if the new interval is
        # overlapping with current interval.
        # Defintion of overlapping is if the end value of new interval is greater than end of current interval
        # If so, merge the two intervals by taking min of beginning value and max of end value of both intervals

        ans = []

        # Iterate through all for the intervals in array
        for i in range(len(intervals)):
            # Base case 1: If new interval is less than beginning interval, 
            # Add new interval to ans array and add rest of intervals as well
            if newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                return ans + intervals[i:]
            # Base case 2: If new interval beginning val is greater than current interval end value
            # Add current interval to ans array as new interval could be overlapping with other intervals
            elif newInterval[0] > intervals[i][1]:
                ans.append(intervals[i])
            # Final case: New interval does overlap with current interval
            # Have to merge the two intervals by taking minimum of new interval and current interval beginning val
            # Take maximum of new interval and current interval's end value
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        # Append newInterval to the ans array after merging with overlapping intervals
        ans.append(newInterval)
        return ans



