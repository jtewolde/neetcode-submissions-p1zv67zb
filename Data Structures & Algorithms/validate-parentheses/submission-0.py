class Solution:
    def isValid(self, s: str) -> bool:
        # Initial Approach:
        # Use a stack data structure to push and pop parenthesis in the string
        # Create a hashmap to map each matching opening and closing parenthesis with each other
        # If the current character is a opening parenthesis, push it to the stack
        # If the current character is a closing parenthesis, pop it out
        # If the stack is empty, then return True. Else, return false

        stack = [] 

        closeToOpen_dict = {")": "(", "}": "{", "]": "["}

        s_list = list(s)
        length = len(s_list)

        for char in s:
            # If the current char is a closing parenthesis
            if char in closeToOpen_dict:
                # If the stack is not empty and the top of the stack is a opening, pop the closing parenthesis
                if stack and stack[-1] == closeToOpen_dict[char]:
                    stack.pop()

                else:
                    return False

            else:
                stack.append(char)
    
        return True if not stack else False
    
