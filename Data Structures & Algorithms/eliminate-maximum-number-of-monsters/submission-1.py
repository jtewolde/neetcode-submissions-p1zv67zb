class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # Approach: Use a Greedy and iteration techinque to determine and eliminate monsters from reaching the city based on their distance and speed
        # Each monster has a distance and speed attached before reaching the city

        # Create minReach array that will store the minute value when the certain monster reaches the city based on distance / speed
        minReach = []

        # Iterate through each dist and speed for each index/monster 
        for d, s in zip(dist, speed):
            # Calculate minuteToReach by dividing d / s, take the ceiling of the result and append to minReach array
            minute = math.ceil(d / s)
            minReach.append(minute)

        # Sort minReach array from least to greatest
        # Initialize ans variable that stores number of monsters eliminated before reaching city
        # Also, iterate through entire length of minReach array for every minuteToReach
        minReach.sort()
        ans = 0
        for minute in range(len(minReach)):
            # Determine if current min val exceeds val in minReach
            # If true, the monster reaches city and return current ans value
            # Otherwise, increment ans by 1 if monster is eliminated
            if minute >= minReach[minute]:
                return ans
            ans += 1
        return ans


