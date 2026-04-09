class MyStack:
    # Approach: Use a Deque to append, pop, and get top elements to simulate as a stack

    # Initialize queue variable by usign deque
    def __init__(self):
        self.queue = collections.deque()

    # Append the x value into the queue to represent pushing into the stack
    def push(self, x: int) -> None:
        self.queue.append(x)

    # Popping out last element from queue for popping from top of stack
    def pop(self) -> int:
        return self.queue.pop()
        
    # Return last element in queue to get the top of the stack
    def top(self) -> int:
        return self.queue[-1]
    
    # See if the length of the queue is zero, return True for being empty
    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else:
            return False
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()