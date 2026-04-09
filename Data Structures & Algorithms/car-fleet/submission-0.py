class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Approach for solving this problem is by using a Stack
        # Synopsis: Take the given position and speed arrays and combine them with zip function to make a singular array
        # Then, reverse and sort the newly created array as we want to start with the car with highest position
        # Calculate the top car's ETA (target-postition)/speed. Append the ETA's to the stack
        # Compare the top car's ETA to other cars, if the other car's ETA is less than the top car's, pop from the stack
        # Return the len of the stack as final answer

        # Combine the position and speed arrays to one
        # Sort the new pairs array and reverse it
        pairs = [(pos, sped) for pos, sped in zip(position, speed)]
        pairs.sort(reverse=True)

        # Create stack to store car's ETA
        stack = []

        # Iterate through each car's position and speed
        # Calcuate the ETA of the current car
        for p, s in pairs:
            ETA = (target - p) / s
            stack.append(ETA)

            # If there are atleast 2 cars in the stack and the car at top of stack ETA is less than next one,
            # Pop from stack as it becomes a car fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)