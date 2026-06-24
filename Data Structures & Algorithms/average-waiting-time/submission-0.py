class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # Approach: Use Iteration/Simulation to simulate chef taking orders from customers
        # The chef can only take one order at a time and makes customers wait if they arrive when the chef is busy
        # Track the current time and accumulate the total waiting time as final answer

        # Initialize variables, currTime, for tracking the current time of chef's simulation of an order
        # Also, track the total waiting time of an order
        currTime = 0
        totalTime = 0

        # Iterate through each customer with their own arrival and order times
        for arrival, order in customers:
            # If the chef's time is busy and greater than the arrival time of order
            # Add extra wait time to the totalTime
            if currTime > arrival:
                totalTime += currTime - arrival
            # Otherwise, set the currTime of chef to equal the arrival time of the incoming ordder
            else:
                currTime = arrival

            # Add the current order time to both total and curr time
            totalTime += order
            currTime += order
            
        # Calculate the average waiting time and return as final answer
        return totalTime / len(customers)