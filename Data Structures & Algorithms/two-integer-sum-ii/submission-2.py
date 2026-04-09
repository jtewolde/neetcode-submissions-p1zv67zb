class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initial Approach with Two Pointers
        # Use the two pointer strategy, using left and right to see if the two indexes equal target
        # If the sum of two pointers greater than target, move right pointer to the left
        # If the sum of two pointers less than target, mover left pointer to the right
        # If the sum is equal to the target, append the indexes of left and right to the ans array.
        # Add one to each of the left and right variables for it to be 1-indexed
        # return ans array for final answer

        left = 0
        right = len(numbers) - 1
        
        ans = []

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                ans.append(left + 1)
                ans.append(right + 1)
                break

        print(ans)
        return ans