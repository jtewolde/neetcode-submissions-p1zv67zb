class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # This optimal approach of solving this problem is by using prefix/postfix approach
        # Synposis: Preinitialize two arrays, prefix and postfix, with zeros and the length of nums
        # Prefix tracks product of nums left of current num
        # Postfix tracks product of nums right of current num
        # Set the 0-index of prefix and last index of postfix to 1 for multiplying to work
        # Create three different, seperate for loops, the first one being for setting values of prefix array
        # Second loop for setting values for postfix array
        # Third loop is for multiplying the pre and postfix values of each index for final ans array

        # Initialize n variable for length of nums, 
        # ans array to store final products, prefix array and postfix array
        n = len(nums)
        ans = [0] * n
        prefix = [0] * n
        postfix = [0] * n

        # Set the zero index of prefix and last-index of postfix to 1
        prefix[0] = postfix[n - 1] = 1

        # First loop: Set the values of prefix array to equal product of number and prefix of previous index
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        # Second loop: Iterate through postfix array in reverse, set values of each postfix index to product of nums and postfix of next index
        for i in range(n - 2, -1, -1):
            postfix[i] = nums[i + 1] * postfix[i + 1]

        # Third loop: Iterate through len of nums array, set each value of ans array to product between prefix and postfix at same index
        for i in range(n):
            ans[i] = prefix[i] * postfix[i]

        return ans



        