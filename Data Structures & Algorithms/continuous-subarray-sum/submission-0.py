class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Approach: Use prefix sums and a hashmap to determine if the nums array has a good subarray and return if true or not
        # A good subarray is a subarray with a length of at least two and sum of elements is multiple of k
        # The hashmap will store the remainders of subarrays with the end index of subarray
        # If the prefix sum up to index i has remainder r when divided by k and prefix sum up to index j has the same remainder
        # Then, the subarray from i + 1 to j has sum that is multiple of k

        # Create hashmap for storing remainder values and their first occurence index
        # Also, create running total variable during iteration
        remainderMap = {0 : -1} # map of remainder -> end index
        total = 0

        # Enumerate through nums array with index and val of each element
        for indx, num in enumerate(nums):
            # Add element val to the running total and compute the remainder
            total += num
            remainder = total % k

            # If the remainder isn't in the map, then store it with current index
            if remainder not in remainderMap:
                remainderMap[remainder] = indx
            # Otherwise, if the remainder exists in the map and the subarray length is at least 2, return true
            elif indx - remainderMap[remainder] > 1:
                return True
        return False

