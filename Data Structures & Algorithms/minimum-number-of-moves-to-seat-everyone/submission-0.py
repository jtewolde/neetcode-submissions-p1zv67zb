class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Goal: The end goal for solving this problem is matching both of seats and students arrays
        # Add/Subtract each student in array to match with seats element at each element
        # Brute Force Approach: Use nested for loops to iterate through both arrays and match elements within arrays
        
        # Greedy Approach: Sort both seats and students array in increasing order
        # With sorting, the leftmost student will match up with leftmost seat and so on
        # Iterate through both arrays with length of seats array
        # Calculate the abs value of difference between the current elements in both array
        # Add result to variable and return as final answer

        # Sort both seats and students array to match elements in both arrays based on relative ordering
        # Initialize ans variable that will keep track of number of minimum moves
        seats.sort()
        students.sort()
        ans = 0

        # Iterate through both arrays using length of seats array
        # Calculate the absolute difference of current elements on seats and students array
        for i in range(len(seats)):
            ans += abs(seats[i] - students[i])
            
        return ans