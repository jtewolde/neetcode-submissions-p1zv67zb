class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # Approach: Change the nums array so elements are tuples with value and index of each element
        # Use a minHeap to get the minimum value in nums
        # Pop out the minimum value and replace it with it being (min value * multiplier)
        # Push the new multipled value into the min heap
        # Use a loop for perform this operation for k times

        # Create a new nums array whose elements are tuples that have the index and value of orignal array
        newNums = [(num, indx) for indx, num in enumerate(nums)]

        # Initialize minHeap using newNums array with tuple elements
        heapq.heapify(newNums)

        # Loop to perform k operations
        for _ in range(k):
            # Pop out minimum value and its index from newNums array
            min_value, min_index = heapq.heappop(newNums)
            # Mutliply element at min index with multiplier 
            nums[min_index] *= multiplier
            # Push updated value into minHeap with its index)
            heapq.heappush(newNums, (nums[min_index], min_index) )
        
        return nums