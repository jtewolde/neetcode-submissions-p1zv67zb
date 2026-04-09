class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Approach for solving this problem is by using a minheap
        # Synposis: By using a minheap, the strategy is to create a empty minheap,
        # Iterate through the nums array.
        # First check if the length of the heap is less than the value of K,
        # If true, then push the current number to the heap
        # If false, then use heapppushpop method to push the current num to the heap while popping out at same time
        # Return the top value from the minHeap

        # Initialize empty array for minHeap
        minHeap = []

        # Iterate through each number in nums array,
        for num in nums:
            # Check if the length of minHeap is less than value of K
            # If true, push current num to the minHeap
            if len(minHeap) < k:
                heapq.heappush(minHeap, num)

            # If false, then still push current num to minHeap
            # Also pop out number from the Heap
            else:
                heapq.heappushpop(minHeap, num)
                
        # Return 0-indexed number from minHeap/top of heap
        return minHeap[0]
