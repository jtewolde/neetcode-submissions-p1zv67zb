class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Optimal Approach: Use a maxHeap to get the max pile in gifts element
        # Find the max element in gifts array, pop it out of max heap
        # Take the floor square root of popped out pile and push it back into maxHeap
        # The top of maxHeap will have new maximum pile that repeats with new second
        # Return the sum of the gifts with new piles

        # Initialize maxHeap using new Python maxHeap with heapify_max for gifts
        heapq.heapify_max(gifts)
        
        # Iterate through heap of gifts for k amount of seconds(iterations)
        for _ in range(k):
            # Pop out the top element in gifts heap that will be maximum element
            gift = heapq.heappop_max(gifts)
            # Push the floor square root of popped out gift back into the heap
            heapq.heappush_max(gifts, floor(sqrt(gift)))
        
        # Take the sum of all elements in gifts heap and return it
        return sum(gifts)