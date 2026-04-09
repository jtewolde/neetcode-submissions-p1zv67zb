class MyQueue:

    # Initialize queue attribute using array data structure that will be used as a stack
    def __init__(self):
        self.queue = []

    # Append the x parameter to the queue like normal
    # The front of the queue is the zero index  
    def push(self, x: int) -> None:
        self.queue.append(x)
        
    # Pop from the front of the queue, being the zero-index
    def pop(self) -> int:
        return self.queue.pop(0)
        
    # Return the element in the front of queue
    def peek(self) -> int:
        return self.queue[0]
        
    # Use the length of the queue to see if it is empty or not
    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()