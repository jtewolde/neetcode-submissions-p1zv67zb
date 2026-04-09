class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Goal: Comparing heights array with expected array which is a sorted version of the heights array
        # Compare each element at the same index to see if they are equal, if equal > add one to res

        # Initialize res variable to keep track of number of indices where both elements in arrays are equal
        # Create expected array that is a sorted version of heights
        res = 0
        expected = sorted(heights)

        # Iterate through both arrays, compare elements at same index i
        # If equal, increment res variable by one
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1

        return res
