class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Approach: Use a hashmap to count the frequencies of each unique num in nums
        # Initialize ans variable that will keep track of number of good pairs created
        # Also, create count hashmap that will keep track of frequencies of each num
        # Iterate through each number in array with for loop
        # If the current num is already in the hashmap
        # Increment ans with the count of that number b/c good pair can be created
        # Also, increment count of num by one
        
        # Initialize ans variable that will keep track of number of good pairs created
        # Also, create count hashmap that will keep track of frequencies of each num
        ans = 0
        count = {}

        # Iterate through each number in array with for loop
        for num in nums:
            # If the current num is already in the hashmap
            # Increment ans with the count of that number b/c good pair can be created
            # Also, increment count of num by one
            if num in count:
                ans += count[num]   
                count[num] += 1
            # Otherwise, make count of current num one
            else:
                count[num] = 1
        return ans