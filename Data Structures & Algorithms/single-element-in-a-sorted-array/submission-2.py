class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Approach: Use binary search and bit manuiplation to search for singular element in nums
        # Initialize left and right pointers to conduct binary search on nums
        # Traverse through nums while left <= right in a loop
        # Calculate the middle pointer with left and right
        # Use XOR operation to compare element at mid to other element next to mid
        # Determine where single element is located using logic of pair pattern
        # Since each element is a pair, then the indices for a new pair would be even always until single element is encountered
        # If nums[mid] has an odd index, then nums[mid ^ 1] will be mid - 1(left side)
        # If nums[mid] has an even index, then nums[mid ^ 1] will be mid + 1(right side)
        # Check if both elements next to each other are equal, if true then search right side by setting left to mid + 1
        # If not, then search left side by setting right to mid - 1

        # Initialize left and right pointers for applying binary search
        left, right = 0, len(nums) - 1

        # Iterate through nums array using left and right pointers
        while left < right:
            # Compute mid pointer
            mid = (left + right) // 2

            # Compare element at mid pointer to element next to it using XOR depending on index
            # Case 1: If both elements aren't equal, then the pair pattern was disrupted 
            # and search the left side to find single element
            if nums[mid] != nums[mid ^ 1]:
                right = mid
            # Case 2: If both elements are the same, then the pair pattern is intact and search the right side
            else:
                left = mid + 1

        return nums[left]