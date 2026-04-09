class Solution:
    def jump(self, nums: List[int]) -> int:
        # Most optimal approach to solve this probleme is with Greedy
        # Create ans variable to keep track of # of jumps made ans final answer
        # Create two pointers, left and right, which represent the current window of indices with current num of jumps
        # Use a while loop where it goes for right pointer hasn't reached the end of array (len(nums) - 1)
        # Initialize farthest variable which stores the farthest jump that a number in the window can jump
        # Iterate through the window of left and right pointers with for loop
        # Set the farthest variable to be the maximum between itself and the jump a number can take, which is index + num[index]
        # Farthest variable wil lbe the next boundary for right pointer
        # Next, move the window down the array, with left pointer moving to right pointer's position  + 1
        # Right pointer will be moved to the farthest's position
        # Additionally, increment ans by 1 to update num of jumps taken so far
        # Return ans as final answer

        ans = 0
        left, right = 0, 0

        while right < len(nums) - 1:
            farthest = 0
            for index in range(left, right + 1):
                farthest = max(farthest, index + nums[index])
            
            left = right + 1
            right = farthest
            ans += 1

        return ans

            