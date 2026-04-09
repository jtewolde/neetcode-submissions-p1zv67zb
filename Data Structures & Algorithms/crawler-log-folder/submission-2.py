class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # Approach: Use a stack data structure to keep track of all file operations
        # Append the main folder first into the stack(Index 0)
        # Iterate through the logs array:
        # If the operation is '../', pop from the top of the stack
        # If the operation is './', don't pop or append to stack
        # Else, append to the stack if it is a valid file operation

        # Initialize stack to put valid child folders
        stack = []

        # Iterate through all of the logs in log array
        for log in logs:
            # If current log is '../', check if the stack is non-empty and pop from stack
            if log == "../":
                if stack:
                    stack.pop()

            # Check if current log is not './' for remaining in folder
            # If not, then append to the stack
            elif log != './':
                stack.append(log)
                
        # Return length of stack as final answer
        return len(stack)