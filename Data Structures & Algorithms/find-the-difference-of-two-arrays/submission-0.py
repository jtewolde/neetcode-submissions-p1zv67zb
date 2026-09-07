class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Approach: Use hash sets to convert each list to hash sets for faster lookup time of O(1)
        
        # Initialize and convert both nums array into hash sets that removes any duplicates in arrays
        # Also, create empty ans arrays that will store elements for each set that isn't in the other
        nums1Set, nums2Set = set(nums1), set(nums2)
        ans1, ans2 = [], []

        # Iterate through every element in nums1Set and check if the element is nums2Set,
        # If not, then append the element into ans1
        for num in nums1Set:
            if num not in nums2Set:
                ans1.append(num)

        # Iterate through every element in nums2Set and check if the element is nums1Set,
        # If not, then append the element into ans2
        for num in nums2Set:
            if num not in nums1Set:
                ans2.append(num)

        # Combine both ans arrays into the single array and return as final answer
        return [ans1, ans2]
