class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Approach: Use Counter data structure to count the frequency of students ans what sandwich they want
        # Initialize cnt variable with Counter to get all of the frequencies of students 
        # depending on the sandwich they want being either 0 or 1
        # Then, create total variable that will store the total amount of students by taking len of array
        # Iterate throgh every value in the sandwich array:
        # See if the count of the current sandwich is greater than zero:
        # If true, decrement count for that value and total variable
        # If false, then simply break from for loop to next value
        # Return remaining value in total

        # Initialize cnt variable with Counter to get all of the frequencies of students 
        # depending on the sandwich they want being either 0 or 1
        cnt = Counter(students)
        total = len(students)

        # Iterate throgh every value in the sandwich array:
        for s in sandwiches:
            # See if the count of the current sandwich is greater than zero:
            # If true, decrement count for that value and total variable
            if cnt[s] > 0:
                cnt[s] -= 1
                total -= 1
            # If false, then simply break from for loop to next value
            else:
                break
        # Return remaining value in total
        return total


