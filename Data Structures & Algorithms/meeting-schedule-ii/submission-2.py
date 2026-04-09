"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Approach for solving this intervals problem is using a MinHeap and sorting
        # Synopsis:
        # Create a minHeap array where it stores intervals based off of overlapping or it
        # Sort the intervals array by their start times to be able to identify overlapping easier
        # Iterate through each interval with for loop
        # Compare the end val inside of heap to current interval's start val, if the end val is less than start val, pop out element
        # Regardless, Heappush current interval's end val inside of heap
        # Return the length of minHeap for final answer
        # The heap will only store intervals that overlap 


        # Sort intervals array by starting times with lambda
        intervals.sort(key = lambda interval: interval.start)

        # Create minHeap array that will store end values of intervals that don't overlap
        minHeap = []

        # Iterate through intervals array
        for interval in intervals:
            # If minHeap is nonempty and the end val of interval inside of minHeap doesn't overlap with current interval,
            # Then, pop the end val out of the minHeap array
            if minHeap and minHeap[0] <= interval.start:
                heapq.heappop(minHeap)
            # Store end val of current interval regardless if minHeap is empty or not
            heapq.heappush(minHeap, interval.end)

        # By default, return true for the case if the array are empty
        return len(minHeap)
