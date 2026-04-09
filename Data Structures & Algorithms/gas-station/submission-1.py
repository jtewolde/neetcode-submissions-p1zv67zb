class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # The approach for solving this problem efficiently is with Greedy
        # Goal is to see if the car can complete loop of gas stations
        # Start by seeing if the sum of gas array < sum of cost array
        # If so, return -1 as circuit can't be completed
        # Create two variables before iterating through gas array
        # startIndex variable to keep track of starting index as the final answer
        # lastGas variable to keep track of the remanining gas from subtracting gas - cost
        # Iterate through the gas array
        # Calculate difference between gas and cost at current index
        # If lastGas is ever less than zero, move start variable up one and reset lastGAs to zero
        # Return startIndex as final answer

        if sum(gas) < sum(cost):
            return -1

        startIndex = 0
        lastGas = 0

        for i in range(len(gas)):
            lastGas += gas[i] - cost[i]

            if lastGas < 0:
                startIndex = i + 1
                lastGas = 0

        return startIndex




