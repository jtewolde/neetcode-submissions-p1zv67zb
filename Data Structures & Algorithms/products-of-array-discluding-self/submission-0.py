class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initial approach for solving this problem is with Brute Force

        # Initialize n variable for length of nums, ans array to store final products
        n = len(nums)
        ans = [0] * n

        # Create nested for loop to iterate through nums array,
        # Initialize product variable to store the total products of nums to 1 for every new num
        for i in range(n):
            product = 1

            for j in range(n):
                # If same index of num is encountered, skip it for including it to the product
                if i == j:
                    continue
                product *= nums[j]

            # Append the product of all nums except current num to ans array at index i
            ans[i] = product

        return ans