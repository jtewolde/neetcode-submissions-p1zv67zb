class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Logic: Divide the nums array into two paritions that equal each other
        # Amount of numbers in a parition doesn't matter
        # Base case is when the sum is zero, meaning no numbers are paritioned
        # If the sum of all numbers in nums are odd, then automatically return false as odds can't be divided into two paritions
        # Create dp set that will store the curTotal of numbers being added with each other
        # Iterate through indexes of nums array in reverse and go through every total in dp set
        # 
        
        # Establish base case of total sum of nums being odd
        if sum(nums) % 2 != 0:
            return False

        # Initialize dp set that stores curTotal of each number in nums with each other to find target value
        # Add zero to set as base case if there are no numbers that sum to zero
        dp = set()
        dp.add(0)

        # Create target variable that represents target that each parition must equal to
        target = sum(nums) // 2

        # Create nested for loop where it goes through nums backwards
        # And goes through each current total in the dp set
        for i in range(len(nums) -1 , -1, -1):
            # Create nextDP to store new totals for each number since originail dp set will be iterated through
            nextDP = set()
            # Add current number in nums to each curTotal value in dp set
            for curTotal in dp:
                nextDP.add(curTotal + nums[i])
                nextDP.add(curTotal)
            # Update original dp with values of nextDP
            dp = nextDP

        # Finally, if the target value is in dp set, return true
        return True if target in dp else False

