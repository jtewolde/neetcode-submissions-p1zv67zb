class Solution:
    def simplifyPath(self, path: str) -> str:
        # Approach for this problem is using a stack to process all characters in path string
        # Use if statements to follow the given rules on slashes and periods to simplify path
        # Return the simplified path as a string

        # Logic: First, split path string for every character to be seperated
        # Iterate through every character in split path string
        # Determine if char follows list of rules for simplified path
        # If so, append to stack
        # IF the current character in splitPath is "..", then pop from stack to represent going back on directory

        # Initialize splitPath that is the splitted path string by forward slash
        # And stack to keep track and process every character
        splitPath = path.split("/")
        stack = []

        # Iterate through every char in splitPath
        for char in splitPath:
            # Deal with any ".." characters in splitPath by popping out top of stack
            # Represents going to previous directory
            if char == "..":
                if stack:
                    stack.pop()
            # Otherwise, append characters into stack as long it is not a single dot or nothing
            elif char != "" and char != ".":
                stack.append(char)
            
        # Create simplified path string by adding forward slash as first character
        # Then, join characters in stack by spliting them with forward slashes
        return "/" + "/".join(stack)



