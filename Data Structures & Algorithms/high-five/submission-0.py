class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # Approach: Use maxHeap data structure to get the top max scores of each student to get average
        # Sort the items array based on student ID to group scores of student adjacent to each other
        # Create solution array to hold subarrays of averages for each student
        # Create a new hashmap where the key is a student's ID and the value is the maxHeap of scores
        # Before calculating averages, iterate through items and push each student's score into their maxHeap
        # Next, iterate through sorted created hashmap by student IDs
        # For each unique student ID, pop out the top 5 scores from maxHeap 
        # Calculate the sum and divide by 5 to compute the average
        # Store the student's ID and calculated avg in a subarray and append to solution array

        # Initialize solution array to store final answers for each student's averages
        # All_Scores to store key-value pair of student ID and maxHeap of scores
        solution = []
        all_scores = defaultdict(list)
        k = 5

        # Before calculating averages, iterate through items and push each student's score into their maxHeap
        for item in items:
            student_ID = item[0]
            score = item[1]
            heapq.heappush_max(all_scores[student_ID], score)

        # Next, iterate through sorted created hashmap by student IDs
        # For each unique student ID, pop out the top 5 scores from maxHeap 
        for student_ID in sorted(all_scores.keys()):
            avg = 0 # Calcuate avg for each student, starting at zero

            # Get the top 5 scores of each student by popping out from maxHeap and append to solution
            for i in range(k):
                avg += heapq.heappop_max(all_scores[student_ID])
            solution.append([student_ID, avg // k])

        return solution

