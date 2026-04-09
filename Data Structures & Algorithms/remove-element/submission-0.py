class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Brute force approach: 
        # Initialize tmp array to store values in nums that aren't equal to val
        # Iterate through entire array, compare val to value at current index
        # If the val is equal to current index, continue to the next number
        # If not equal, append that num to tmp

        # Initialize temp array to store nums that aren't equal to val
        temp = []

        # Go through every number in nums and append num that isn't equal to val
        # Else, if it does, continue
        for num in nums:
            if num == val:
                continue
            temp.append(num)
        
        # Iterate through temp array with index
        # Set the nums at current indx to value of temp[indx]
        for indx in range(len(temp)):
            nums[indx] = temp[indx]
        return len(temp)
        

        return len(nums)

