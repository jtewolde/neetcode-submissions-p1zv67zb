class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Logic: Merge both nums array into the nums1 array with sorting algorithm
        # Approach: Use two pointers approach by putting pointers at the end of each array
        # Compare the values at each pointers, merge values in reverse as accordingly

        # Start at the end of the merged array
        last_index = m + n - 1

        # Merge nums1 and nums2 in reverse order by starting at end
        while n > 0 and m > 0:
            # Compare values at end of each nums array,
            # Place appropriate number into current index
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last_index] = nums1[m - 1]
                m -= 1
            else:
                nums1[last_index] = nums2[n - 1]
                n -= 1

            last_index -= 1

        # Fill remaining nums1 with leftover elements in nums2
        while n > 0:
            nums1[last_index] = nums2[n - 1]
            n -=1
            last_index -= 1




