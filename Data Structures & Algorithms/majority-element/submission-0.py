class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Logi: Find and return the element that appear more than half of the time in the nums array
        # Approach: Use a Counter to get all of the frequencies/counts of each number in nums
        # Iterate through the items onf the Counter:
        # Check if the value of the certain number is greater than len(nums) // 2
        # If true, return that number. Else, continue

        # Initialize half variable that represnts half of nums array
        # and Count key-value data structure
        half = len(nums) // 2
        count = Counter(nums)

        for num, val in count.items():
            if val > half:
                return num
            else:
                continue

        