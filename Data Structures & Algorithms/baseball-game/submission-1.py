class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Approach: Use a stack to keep track of the score of baseball game by adding, removing, doubling scores
        # Logic: Iterate through operations array, depending on operation string
        # If string in ops is a num, add numerical value of string to stack
        # If string in ops is +, add top two nums on stack and add result to stack
        # If string is "C", pop out previous score from stack
        # If string is "D", double top of stack and append to stack
        # Final answer is sum of all nums in stack

        # Initialize stack data structure to keep track of scores
        stack = []

        # Iterate through all strings in operations
        for op in operations:
            # If curr str is a "+", add top two nums in stack and append result to stack
            if op == "+":
                result = stack[-1] + stack[-2]
                stack.append(result)
            # If curr str is "C", pop out top of stack
            elif op == "C":
                stack.pop()
            # If curr str is "D", double num on top of stack and append to stack
            elif op == "D":
                result = stack[-1] * 2
                stack.append(result)
            else:
                stack.append(int(op))

            print(stack)

        return sum(stack)