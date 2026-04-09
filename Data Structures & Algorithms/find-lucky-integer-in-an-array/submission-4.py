class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # Approach: Use Counter to get all of the frequenices of each value in arr array
        # Iterate through the frequencies and value of each number in arr
        # If a number's freq and val are equivalent, return that number as lucky integer
        # If there are multiple lucky integers, return the largest out of them
        # If there are none, return -1

        # Initialize counter data structure for arr to get all frequencies of each number in arr
        # Lucky variable that keeps track of largest lucky number in arr
        countArr = Counter(arr)
        lucky = 0

        print(countArr)

        # Iterate through items in countArr to get each key-value pair of (freq,val)
        for num in countArr.items():
            # Compare freq and val of number to see if they are equal
            # Update lucky variable to maximum val of lucky numbers
            if num[0] == num[1]:
                lucky = max(lucky, num[1])
                print(lucky)

        if lucky != 0:
            return lucky
        else:
            return -1
