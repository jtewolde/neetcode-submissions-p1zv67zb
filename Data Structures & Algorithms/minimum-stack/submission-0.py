class MinStack:
    # Approach for solving this min stack problem is to use two stacks
    # One stack is a normal stack that pushes and pops given values
    # Second stack is to track the current minimum value at each state

    def __init__(self):
        self.stack = []
        self.minStack = [float('inf')]
        
    # When pushing element:
    # Push element into regular stack normally
    # For minStack, add the minimum between new element and current minimum(top of minStack)
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(min(val, self.minStack[-1]))

    # When popping elements out of stacks:
    # Pop out top element for both regular and minStack
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    # Return the top element from the regular stack
    def top(self) -> int:
        return self.stack[-1]
        
    # Return the top element from the min stack    
    def getMin(self) -> int:
        return self.minStack[-1]
        
