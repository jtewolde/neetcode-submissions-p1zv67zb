class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Synposis: nums1 is a subset of nums2, meaning that all of the elements in nums1 appear in nums2 in some order
        # Goal: For every element in nums1, find out if there is a greater element to the right of it in nums2
        # Approach: Use a monotonic stack, where we first iterate through nums2 in reverse to find next greater element for each value.
        # Store the result in a hashmap to be used for look up on nums1

        # Initialize stack data structure to store potential next greater elements
        # and dictionary to store the mapping of each nums1 element to its next greater element
        stack = []
        dic = {}

        # Traverse through nums2 array in reverse from right to left
        for num in nums2[::-1]:
            # Clean the stack while there is something in stack
            # If the top element in stack is less than current number, then pop out stack as it isn't a next greater element
            while stack and stack[-1] < num:
                stack.pop()

            # Any remaining element in the stack is the next greater element for that element
            # If true, then map the current element to its next greater element
            if stack:
                dic[num] = stack[-1]

            # Process the current element into the stack by appending to see if it s a potential greater element
            stack.append(num)

        # Build the result by looking the mapping of the next greater element for each number in nums1 array
        return [dic.get(num, -1) for num in nums1]
