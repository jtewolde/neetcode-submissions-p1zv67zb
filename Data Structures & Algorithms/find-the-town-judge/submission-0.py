class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Approach: Use indegree and outdegree graph concepts to find town judge in trust array
        # Conditions for town judge is where incoming edges are n - 1(all trust them)
        # Outgoing edges are 0 for judge, they trust no one
        # Initialize two hashmaps for tracking incoming and outcoming edges
        # Iterate through all trust pairs using src and dstn pointer variables:
        # Increment both outgoing/incoming edge for source/destination node by 1 (outgoing[src] += 1) (incoming[dstn] += 1)
        # Then, create for loop for iterating through every n value from 1 to n + 1:
        # Determine if current n value meets the conditions of being town judge
        # Where incoming = n - 1 and outcoming = 0, return indx value
        # otherwise, return -1 if no value is found

        # Initialize two hashmaps for tracking incoming and outcoming edges
        incoming, outcoming = defaultdict(int), defaultdict(int)

        # Iterate through all trust pairs using src and dstn pointer variables:
        for src, dstn in trust:
            # Increment both outgoing/incoming edge for source/destination node by 1
            outcoming[src] += 1
            incoming[dstn] += 1

        # Then, create for loop for iterating through every n value from 1 to n + 1:
        for indx in range(1, n + 1):
            # Determine if current n value meets the conditions of being town judge
            # Where incoming = n - 1 and outcoming = 0, return indx value
            if incoming[indx] == n - 1 and outcoming[indx] == 0:
                return indx
                
        # Otherwise, return -1 if no value is found
        return -1
