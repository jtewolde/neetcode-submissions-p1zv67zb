class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # First brute force approach:
        # Initialize left and right pointers, also create numOfBoats variable to keep track of min number of boats
        # Sort the people array from least to greatest
        # Use two pointers method to compare largest val to smallest val
        # See if the largest val in people array fits within limit, get the difference between the two
        # See if num at left pointer can fit in boat when it is less than right pointer and remaining value

        # Initialize left and right pointers and numOfPeople variable
        left, right = 0, len(people) - 1
        numOfPeople = 0

        # Sort people array from smallest to largest
        people.sort()

        # Set up two pointers on people artay
        while left <= right:
            # Get the remaining space on boat by getting difference between limit and largest person
            # Set right pointer inward and add one to numOfPeople array
            remaining = limit - people[right]
            right -= 1
            numOfPeople += 1

            # See if person at left can fit in same boat by making sure that val at left is not bigger than remaining space
            if left <= right and people[left] <= remaining:
                left += 1

        return numOfPeople


