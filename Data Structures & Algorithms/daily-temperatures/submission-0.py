class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initial Approach using stack:
        # Create a stack variable to store temperatures
        # Create a result array that stores the # of days that a warmer temperature appears
        # Iterate through the temperatures array using enumerate for loop
        # If the current temp is less than next temp, push to stack
        # If the current  temperature is greater than other elements in stack, 
        # Pop elements from stack until top element of stack is not less than current element
        
        stack = [] # 
        result = [0] * len(temperatures) # Zeros default for unpopped temp 

        # Use enumerate for loop to keep track of index and temperature values easily
        for ind, temp in enumerate(temperatures):
            # while stack is not empty and the current temp > top of stack element
            while stack and temp > stack[-1][0]:
                # Pop both index and temp values of current temp from stack
                stackTemp, stackInd = stack.pop()
                # Subtract current temp's index to top stack element's index and add to stack
                result[stackInd] = (ind - stackInd)
            stack.append([temp, ind])
        return result



