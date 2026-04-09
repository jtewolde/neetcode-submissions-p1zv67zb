class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Approach for this problem by using fast and slow pointers with linked lists
        # First, start off initializing fast and slow pointers at 0 index of nums
        # Use a while true loop to prove that there is a cycle in the array, meanign there is a duplicate
        # Set slow pointer to what it is pointing at: nums[slow]
        # Advance fast pointer two spaces using nums[nums[fast]] to advance
        # See if the fast and slow are equal to each other, if so -> break out of loop, proving there is a cycle
        # Create another separate slow pointer that starts at 0-index of nums
        # Use a while true loop to go through entire nums array
        # Set both slow pointers to what they are pointing to in nums array
        # If the two slow pointers are set equal to each other, return slow

        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow




