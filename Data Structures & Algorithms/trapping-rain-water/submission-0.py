class Solution:
    def trap(self, height: List[int]) -> int:
        # Approach for solving this problem is to use the Two-Pointes Algorithim
        # Synposis: For tihs problem, the goal is to calculate the total amount of water that is trapped between bars
        # Water can be trapped between bars when the left and right walls are taller than height of water
        # However, the height of water at a position is bounded to the height of the smallest wall on both sides
        # Example: Bathtub where height of water in tub is bounded to smallest height of border before overflowing
        # The final answer will be the total amount of trapped water where valid indices
        
        # Pre-initialize left and right pointers to be used in problem
        n = len(height)
        left = 0
        right = n - 1
        total = 0

        # Initialize variables that track the max height of left and right walls from current position in heights
        leftMax, rightMax = 0, 0

        # Create while loop that uses two pointers approach to iterate through heights array
        while left < right:
            # See whether left or right wall is restricting height of water
            if height[left] < height[right]:
                # See if height at left pointer is greater than current max on left of current position
                if height[left] > leftMax:
                    # Set max height observed on left to current height on left pointer
                    leftMax = height[left]
                else:
                    # Otherwise, add to total variable by 
                    total += leftMax - height[left]
                # Move left pointer inward
                left += 1
            
            # The scenario where the right wall is the smaller wall, restricting height
            else:
                # See if height at right pointer is greater than current max on right of current position
                if height[right] > rightMax:
                    # Set max height observed on right to current height on right pointer
                    rightMax = height[right]
                else:
                    # Otherwise, add to total 
                    total += rightMax - height[right]
                # Move right pointer inward
                right -= 1

        return total
                
