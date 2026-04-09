class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Approach for solving this problem is with sorting intervals array and merging
        # Synopsis: Sort the intervals array first by their starting points
        # Iterate through intervals array for each interval
        # Compare two intervals too see if they overlap or not
        # Overlapping is when the end val of the first interval is greater then the start val of second interval
        # first[1] >= second[0] is overlapping

        # Initialize merged array, where all intervals including merged intervals will be appended to
        merged = []

        # Sort intervals array by their starting points
        intervals.sort(key = lambda interval: interval[0])

        # Iterate through every single interval in array
        for interval in intervals:
            # Base case: If there is nothing to compare current interval to in merged, append to merged
            # Also, if there is no overlapping, just append current interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Otherwise, merge the two intervals by keeping the start the same from merged
                # End point of merged interval is the maximum between current index's end and merged's
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]

        return merged

