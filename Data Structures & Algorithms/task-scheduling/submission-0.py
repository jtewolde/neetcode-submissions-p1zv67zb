class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Approach for solving this problem is to use a MaxHeap and a queue 
        # Synposis: Going to use a MaxHeap to trakc the max frequency of certain tasks as we start with the most
        # Go back and forth between Heap and the queue, pushing and popping tasks depending on time
        # At the end, return the time to go through all tasks

        # Preinitialize queue structure used, get count of all tasks to get frequency and time
        count = Counter(tasks)
        queue = deque() # Pairs: [-cnt, time + n]
        time = 0

        # Create maxHeap with neg values to be maxHeap and heapify it
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        # Perform while maxHeap or queue is not empty
        # Increment time variable by one each time
        while maxHeap or queue: 
            time += 1

            # If there are tasks in maxHeap, 
            # Pop out freq of task and add one to decrement as it is negative
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                
                # If the count of a certain task is nonzero, append to queue as pair with idle time
                if cnt:
                    queue.append([cnt, time + n])

            # Otherwise, if there are no tasks remaining in heap, 
            # set the time variable to the idle time of top task in queue
            else:
                time = queue[0][1]

            # If there are tasks in the queue and the idle time of task equals the current time
            # Meaning, the task is no longer in idle, push the count of task back to the heap
            if queue and queue[0][1] == time:
                newTask = queue.popleft()[0]
                heapq.heappush(maxHeap, newTask)

        return time


