class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Logic for solving this problem with Stack:
        # Iterate through the tokens array
        # If it encounters a number, push it into the stack
        # If it encounters a operator, pop two recent numbers out of the stack
        # Solve the mathemical problem between the operator and two numbers
        # Push the result back into the stack
        # Return the remanining integer from the stack

        stack = []
        equation = ""
        operators = {"+","-","/","*"}

        for char in range(len(tokens)):
            # If the current char is a number, add to stack
            if tokens[char] in operators: 
                # Pop last two elements from stack, store them in elements variables
                element1 = stack.pop()
                element2 = stack.pop()
                print("stack after pop", stack)
                
                if tokens[char] == '+':
                    stack.append(element1 + element2)
                elif tokens[char] == '-':
                    stack.append(element2 - element1)
                elif tokens[char] == '*':
                    stack.append(element2 * element1)
                elif tokens[char] == '/':
                    stack.append(int(float(element2) / element1))
            else:
                stack.append(int(tokens[char]))
                
                print("stack after result", stack)
                

        return stack.pop()