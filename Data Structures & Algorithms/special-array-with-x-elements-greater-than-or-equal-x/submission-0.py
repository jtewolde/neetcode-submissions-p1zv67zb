class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # Approach: Use sorting and two pointers to find a special number while iterating through nums array
        # Determine if current number has the same amount of greater elements in nums array
        
        # Sort the nums array and initialize two pointers, arrPointer for iterating through nums array
        # CV represents the current candidate value to see if current candidate is valid
        nums.sort()
        n = len(nums)
        arrPointer = 0
        cv = 1

        # Iterate through nums array while both pointers are within valid boundaires
        while arrPointer < n and cv <= n:
            while arrPointer < n and cv > nums[arrPointer]:
                # Advance pointer past all elements that are smaller than cv pointer
                arrPointer += 1

            # Check if the count of the remaining elements equals the current cv pointer,
            # If so, return cv as final answer
            # Otherwise, increment cv to the next candidate
            if cv == n - arrPointer:
                return cv
            cv += 1
        # Return -1 if there is no special value 
        return -1
