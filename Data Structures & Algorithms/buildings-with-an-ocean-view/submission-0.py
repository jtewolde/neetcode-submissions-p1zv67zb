class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # Approach: Use a Greedy approach by iterating through heights array in reverse
        # By starting with rightmost element, the building will always have a ocean view
        # Create a max variable that stores the running maximum height encountered during traversal
        # Compare current element with running max, if current height > max, then add index to ans array
        # Otherwise, skip the building as it doesn't have a ocean view

        # Initialize runningMax to keep track of current max height encounterd in traversal
        # Ans array for storing index of building that have ocean view
        runningMax = 0
        ans = []

        # Iterate through heights array by going through it in reverse
        for i in range(len(heights) -1, -1, -1):
            # Case 1: If height of current building is greater than max, append index to ans array and update runningMax
            if heights[i] > runningMax:
                ans.append(i)
                runningMax = max(runningMax, heights[i])
            # Case 2: Skip building element if building doesn't have ocean view
            else:
                continue

        # Reverse ans array for final answer because of reversal traversal and return ans
        ans.reverse()
        return ans

            