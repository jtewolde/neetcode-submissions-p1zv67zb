class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Approach for solvin this problems is to use a Max Heap
        # Synposis: Create an output array that keeps track of all max elements in each window
        # Create a maxHeap where it stores tuples that contain the negative value of num and its index
        # Iterate through nums array
        # Determine if tuples in maxHeap are outdated/out of window, pop them out of MaxHeap
        # Append the current top val on maxHeap to output array as it is the maximum for that window

        # Initialize both heap and output empty arrays, and n for length of nums
        heap = []
        output = []
        n = len(nums)

        # Iterate through entire nums array for every number
        for i in range(n):
            # Push tuple of -val of num and index to maxHeap
            heapq.heappush(heap, (-nums[i], i))

            # Check if the index of current num is outside of window
            if i >= k - 1:
                # Remove outdated elements if top of heap is outside of window
                # Window: [i - k + 1, i]
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                
                # Append top of maxHeap to output array, also turning it back positive
                output.append(-heap[0][0])

        return output

