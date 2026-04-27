class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Approach: Use hashset to store the numbers that are seen in both nums1 and nums2
        # Initialize seen hashset that already has content of nums1 inside
        # Also, create ans array that will store nusm that intersect between both arrays
        # Iterate through every number in nums2
        # Determine if current num is in seen set and already in nums1
        # If true, then append current num into ans array and remove number from seen set
        # Return ans as final snaswer

        # Initialize seen hashset that already has content of nums1 inside
        # Also, create ans array that will store nusm that intersect between both arrays
        seen = set(nums1)
        ans = []

        # Iterate through every number in nums2
        for num in nums2:
            # Determine if current num is in seen set and already in nums1
            if num in seen:
                # If true, then append current num into ans array and remove number from seen set
                ans.append(num)
                seen.remove(num)
        return ans