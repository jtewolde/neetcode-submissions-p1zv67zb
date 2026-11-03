class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Approach: Use a BFS approach and an queue to iterate through each employee node under the manager node
        # Track the ID and the time needed to reach each employee inside of the queue as a tuple
        # Return the final answer for the max time to reach all employees from the head node

        # Create adjacency list to store and map the manager node to its employee nodes with empty list
        adjList = defaultdict(list)
        for idx in range(n):
            adjList[manager[idx]].append(idx)

        # Initialize queue with the tuple of the headID and 0 for time to reach it in graph since it started there
        queue = deque([(headID, 0)])
        ans = 0

        # Use BFS by iterating through the queue
        while queue:
            i, time = queue.popleft()
            ans = max(ans, time)
            for emp in adjList[i]:
                queue.append((emp, time + informTime[i]))
        return ans
