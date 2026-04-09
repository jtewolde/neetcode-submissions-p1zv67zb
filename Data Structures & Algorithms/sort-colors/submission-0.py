class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Approach for solving this problem is by using three pointers to arrange the nums in array to correct section
        # The idea of using three pointers is to essentially parition the array to three sections
        # One section for the zeros, another for the ones, and lastly for the twos
        # Initialize three pointers, two of them are indicate the boundary of each section
        # Pointer Z: index at the rightmost edge/boundary where zeros should be
        # Pointer T: index at the leftmost edge/boundary where twos should be
        # Pointer S: Scan across the nums array to see if each number is in the correct place
        # Logic: Scan through the entire array with pointer T, compare current number at T with 0, 1, 2.
        # If current number == 0 > Increment pointer Z by one to expand area and swap numbers
        
        # Initialize pointers/boundaries for sections of nums array
        # Left Poiners will be -1 because there are no zeros yet
        left_bound = -1
        right_bound = len(nums)
        current = 0

        # Scan through entire array until right boundary is reached
        while current < right_bound:
            # Case 1: Current number is zero, move to left boundary
            if nums[current] == 0:
                # Expand left boundary to include zero
                # Swap numbers to correct positions
                # Increment current position by one to move to next index
                left_bound += 1
                nums[current], nums[left_bound] = nums[left_bound], nums[current]
                current += 1

            # Case 2: Current number is wo, move to right boundary
            elif nums[current] == 2:
                # Expand right boundary by decrementing pointer by one to include two
                # Swap numbers to correct positions
                # Don't increment current pointer b/c swapped numbers need to be examined
                right_bound -= 1
                nums[current], nums[right_bound] = nums[right_bound], nums[current]

            # Case 3: Current number is one, meaning move on to next number as it is in the right place
            else:
                # Increment current by one b/c 1 is in middle position
                current += 1




        