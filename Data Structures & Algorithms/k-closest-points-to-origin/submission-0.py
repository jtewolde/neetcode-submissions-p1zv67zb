class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Approach for solving this problem is by using a MinHeap
        # Initialize two arrays, one for MinHeap which will be heapify later, ans for final answer
        # Iterate through the points array, perform Euclidean distance using both x and y variables
        # Append the distance result and the x-y coordinates to the minHeap array
        # Heapify the minHeap array to convert it to the heap data structure
        # Create a while loop where it uses the k variable as a counter
        # Pop out the distance and x-y coordiantes from minHeap
        # Append only the x-y coordinates to the ans array
        # Decrement k to count down
        # Return ans as final answer

        minHeap = []
        ans = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)

        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            ans.append([x, y])
            k -= 1

        return ans    


        