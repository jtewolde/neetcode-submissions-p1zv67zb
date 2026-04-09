class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Goal: Find and return the elements inside of nums array in which their frequency is greater than
        # n /3 (len(nums) // 3).
        # First Approach: Use Counter data strucutre to get all of the counts for each number in the nums array
        # Iterate through count.items with number and freq being tracked
        # Append numbers in which the frequency is greater than n (len(nums) // 3)
        # Return ans array as final answer

        # Initialize ans array for final answer, count for getting count for each number, and n for 1/3 of numbers
        ans = []
        count = Counter(nums)
        n = len(nums) // 3

        # Iterate through items in count array that gets each number and freq
        for num, freq in count.items():
            # Find valid numbers which freq are greater than 33% of nums array, append to ans array
            if freq > n:
                ans.append(num)
            else:
                continue
        
        return ans