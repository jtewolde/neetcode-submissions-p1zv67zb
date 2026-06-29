class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Approach: Use a hashset/counter to get the frequency of each number in nums array
        # Then, sort the entire nums array accordingly to the frequency increasing
        # The lower frequency comes first in the sorted array
        # If two numbers have the same frequency, compare the values with the larger one comes first

        count = Counter(nums)
        nums.sort(key=lambda n: [count[n], -n])
        return nums