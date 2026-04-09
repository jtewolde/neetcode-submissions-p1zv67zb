class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # The approach for solving this problem is by using two pointers
        # Synposis: Sort the given nums array, 
        # Enumerate each element as the first element in triplet
        # Teriminate early if the first element of sorted array is greater than 0, as it cant make valid triplets
        # See if there are any duplicates of the first elememnt, continue on as we already processed first element to triplet
        # Start two pointers search with left pointer starting after fixed element, right pointer at end of nums array
        # Find valid triplets by calculating sum of triplet and compare it to zero.
        # If sum < 0, move left pointer to right. If sum > 0, move right pointer left. Else, current triplet is valid and append to ans array
        # Move both pointers and continue to increment/decrementing while left < right and there are no duplicates next to current num at pointers

        # Preinitialize variables and arrays for final answers and sorting nums array
        ans = []
        n = len(nums)
        nums.sort()

        # Iterate through nums array, starting at first element
        for i in range(n - 2):
            # Early teriminate if first element is positive
            if nums[i] > 0:
                break

            # See if there any duplicates of first element, skip them
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize left and right pointers
            left, right = i + 1, n - 1

            # Get the current sum of potential triplet
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Compare val of current sum to zero, move left/right pointers accordingly
                # If sum of triplet is zero, append the three elements in an array and into the ans array
                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    
                    # Move left and right pointers inward
                    left += 1
                    right -= 1

                    # Skip the duplicates for the second and third elements
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    
        return ans


        





