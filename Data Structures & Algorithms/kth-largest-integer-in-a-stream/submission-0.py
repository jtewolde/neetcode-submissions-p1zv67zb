class KthLargest:

    # Use minHeap data structure to solve this problem
    # Initialize member variables for self.minHeap being nums and self.k = k
    # For constructor function, insert nums array into minHeap and heapify it
    # Make the minHeap to have a size of k;
    # Create a while loop where while the size of minHeap > k, pop out smallest element
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    # For add function, heappush val into the minHeap from constructor
    # Create a if statement to see if size of minHeap > k,
    # If true: do a heappop on minHeap
    # Else: return the smallest val in minHeap, return index 0 as it is sorted
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]






        
