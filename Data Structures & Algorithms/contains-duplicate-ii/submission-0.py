class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Logic: Search for two numbers in array that are duplicates but are in distinct indices
        # To return true, compare the indices by making sure that the absolute value of the difference
        # Between both indices is less than or equal to given K variable
        # Approach: Use Sliding Window techinque to find duplicates
        # For sliding window approach, use hashset to represent window
        # Add and remove nums from window set when moving through nums array until you find indices that are duplicates

        # Initialize window using hashset and left pointer
        window = set()
        left = 0

        # Use right pointer to iterate through nums array
        for right in range(len(nums)):

            # Make sure if window size is valid by doing abs(left - right) <= k
            # If window size isn't valid, remove left most num in window and move left pointer by one
            if right - left > k:
                window.remove(nums[left])
                left += 1

            # Check if number at right pointer is already in window,
            # Means that the duplicate is already in there
            if nums[right] in window:
                return True

            # Append num at right into the window
            window.add(nums[right])

        return False