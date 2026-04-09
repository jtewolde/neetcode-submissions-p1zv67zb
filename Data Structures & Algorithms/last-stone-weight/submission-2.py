class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Use MaxHeap data structure to solve this problem
        # Create maxHeap structure by heapifying stones array
        # Multiply all values in heap to convert the maxHeap where heaviest stones will be first
        # Compare first two indexs of maxHeap by popping them out of heapq
        # If they are equal, pop out both stones, by default, they are already popped out
        # If x < y, stone x will be popped out and stone y's val will be the difference between y - x
        # Heappush the difference back into the heap
        # Use a while loop for this until there is either one stone remaining or 0 if none
        # Outside of loop, append 0 into the stones array in the case where no stones are available
        # Return the 0-indexed value in stones

        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first < second:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])

