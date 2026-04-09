class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Brute force approach for solving this problem
        # Initialize ans array that had twice the length of nums array
        # Create nested for loop where first loop is going through every num in nums
        # Second for loop: Iterate through that number twice
        # Append current num into ans array

        ans = []

        for i in range(2):
            for num in nums:
                ans.append(num)

        return ans