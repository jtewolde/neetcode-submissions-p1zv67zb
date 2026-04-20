class Solution:
    def check(self, nums: List[int]) -> bool:
        # Synposis: Determine if the given nums array was sorted before and rotated num of times
        # Approach: Use iteration on nums array to find breakpoints where the current element is greater than next
        # Initialize counter variale for counting the number of break points in nums array
        # Create for loop to iterate through nums array
        # Compare the current element to the next element using modular division to wrap around array
        # If current element is greater than next, increment counter as breakpoint
        # If the counter variable ever exceeds 1, return False as there shouldn't be more than 1
        # Return true after iterating thorugh entire pair in nums array with breakpointCount being 1

        # Initialize counter variale for counting the number of break points in nums array
        breakpointCount = 0
        n = len(nums)

        # Create for loop to iterate through nums array
        for i in range(n):
            # Compare the current element to the next element using modular division to wrap around array
            # If current element is greater than next, increment counter as breakpoint
            if nums[i] > nums[(i + 1) % n]:
                breakpointCount += 1
                # If the counter variable ever exceeds 1, return False as there shouldn't be more than 1
                if breakpointCount > 1:
                    return False

        # Return true after iterating thorugh entire pair in nums array
        return True
                