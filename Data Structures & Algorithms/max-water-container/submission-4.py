class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Initial Approach using Two Pointers method
        # Create left and right variables: left = 0 and right = len(heights) - 1
        # Create ans variable for final answer

        # While left < right: compute the area between those two pointers
        # area = width * height where width = right - left
        # height = min(height[r], height[l])
        # Area = (right - left) * min(height[r], height[l])
        # Then, let ans be equal to the max between area and current ans value

        # Finally, if the height of left pointer < height of right pointer
        # Move the left pointer up one (+ 1)
        # Else, Move the right pointer back one (- 1)
        # Then, return ans outside of loop

        left = 0
        right = len(heights) - 1
        ans = 0

        while left < right:
            width = right - left
            height = min(heights[right], heights[left])
            area = width * height
            ans = max(area, ans)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return ans
