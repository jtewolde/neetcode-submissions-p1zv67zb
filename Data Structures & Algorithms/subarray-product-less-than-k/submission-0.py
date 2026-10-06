class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Approach: Use the sliding window techinque to construct continous subarrays using left and right pointers
        # Determine if the product of the current subarray is less or greater than the value of k
        # If greater, then reduce the product by dividing the num at left pointer and increment left pointer up
        # Then, count the num of valid subarrays be using right - left + 1 to count full subarray and other individual nums

        # Initialize needed variables like ans for counting subarrays, 
        # 1 for product for base val, and left pointer at zero index
        ans = 0
        product = 1
        left = 0

        # Iterate through each number in nums array using right pointer
        # Increase product var with current num at right pointer
        for right in range(len(nums)):
            product *= nums[right]

            # Use loop to determine if current subarray's product is greater than value of k
            while left <= right and product >= k:
                # Reduce current product by dividing num at left pointer and increment left pointer
                product = product // nums[left]
                left += 1
            # Increment ans with the count of the current sub array 
            ans += (right - left + 1)
        return ans