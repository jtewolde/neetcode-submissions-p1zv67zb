class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Initial Approach using Stack and Backtracking:
        # Create counters for open and close parentheses

        # Conditions for open and close parentheses are that there are n open and n closed parentheses
        # In order to valid parentheses, the close counter has to be less than open counter when adding close parethesis
        # When adding open parenthesis, open < n
        # When addng closing parenthesis, close < open
        # Valid parenthesis when open == close == n

        # Create stack to keep track of parenthesis / Result to add parenthesis to array and convert to string
        stack = []
        res = []

        # Create backtracking function for recursion to get all valid parenthesis options
        # Follow all of the conditions above
        def backtrack(openNum, closeNum):
            
            # Valid parenthesis when open and close parenthesis count are the same
            if openNum == closeNum == n:
                res.append("".join(stack))
                return

            # Adding opening parentheses to stack and res array
            if openNum < n:
                stack.append("(")
                backtrack(openNum + 1, closeNum)
                stack.pop()

            # Adding all of the closing parentheses to stack and res array
            if closeNum < openNum:
                stack.append(")")
                backtrack(openNum, closeNum + 1)
                stack.pop()

        # Start by 0
        backtrack(0, 0)
        
        return res
