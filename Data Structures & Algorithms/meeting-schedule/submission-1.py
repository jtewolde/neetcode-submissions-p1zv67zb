"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Approach for solving this intervals problem is using Greedy and sorting
        # Synopsis: Sort the intervals array by their start times to be able to identify overlapping easier
        # Compare two intervals, if the first interval's end time is greater than second interval's end time
        # If true, return True, else return False


        # Sort intervals array by starting times with lambda
        intervals.sort(key = lambda interval: interval.start)

        # Iterate through intervals array
        for i in range(len(intervals) - 1):
            # See if there is any overlapping between the two adjacent intervals
            # Return false if there is overlapping
            if intervals[i].end > intervals[i + 1].start:
                print("Start", intervals[i].start)
                print("End", intervals[i].end)
                return False
        
        return True
