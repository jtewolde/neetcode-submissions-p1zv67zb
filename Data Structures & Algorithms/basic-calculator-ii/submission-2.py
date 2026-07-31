class Solution:
    def calculate(self, s: str) -> int:
        # Approach: Use a stack to evaluate expressions in the given parsed string
        # With this problem, PEMDAS is still important as multiplication/division must be done first before addition and subtraction.
        # For '+' and '-', push the numbers onto the stack, negative for subtraction
        # For '*' and '/', pop the previous number from the stack, compute the result and then push it back into the stack.
        # Finally, sum the entire stack to give the final answer.

        # Initialize empty stack and remove all spaces in the expression string
        stack = []
        s = s.replace(' ', '')

        # Initialize num with zero to track current number and the previous operator,   which will start with +
        num = 0
        op = '+'

        # Iterate through each character in the given expression string
        for indx, char in enumerate(s):
            # If the char is a digit, then build and convert it to a number
            if char.isdigit():
                num = num * 10 + int(char)

            # If the current char isn't a digit or reached the end of the string
            # Either append + or -num to stack for addition and subtraction
            # Or calculate result from multiplication or division with current num.
            # Then append back to the stack
            if (not char.isdigit()) or indx == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    prevNum = stack.pop()
                    stack.append(prevNum * num)
                else:
                    prev = stack.pop()
                    stack.append(int(prev / num))

                # Reset the current num and update the previous operator
                op = char
                num = 0
                
        return sum(stack)