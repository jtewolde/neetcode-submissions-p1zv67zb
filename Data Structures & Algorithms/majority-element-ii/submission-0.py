class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Goal: Find and return the elements inside of nums array in which their frequency is greater than
        # n /3 (len(nums) // 3).
        # Brute Force Approach: Iterate through the nums array for every number inside
        # Find the count for each number, if the count is greater than n/3, add to ans array

        ans = []
        count = Counter(nums)
        n = len(nums) // 3

        for num, freq in count.items():
            if freq > n:
                ans.append(num)
            else:
                continue
        
        return ans