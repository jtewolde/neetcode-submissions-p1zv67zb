class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Approach: Use a stack and iteration to pop out consective k chars from string
        # Initialize stack data structure to pairs of chars and their associated count(['a', 1])
        # Iterate through each char in the string and create count vairable to keep track of count of each char
        # If the stack isn't empty and the current char of the pair is the current char, 
        # Increase the count of the char by one. ['a', 2] -? ['a', 3]
        # Otherwise, push the current char into the stack with a count of 1 as it is the first instance
        # Then, check if the count of current char equals the value of k
        # If true, pop from the top of stack
        # Outside of loop, build new and final stirng by iterating through each char and count from stack
        # For every char, put into the ans string for count times.

        # Initialize stack data structure to pairs of chars and their associated count(['a', 1])
        stack = []

        # Iterate through each char in the string
        for char in s:
            # If the stack isn't empty and the current char of the pair is the current char
            # Increase the count of the char by one. ['a', 2] -? ['a', 3]
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1

            # Otherwise, push the current char into the stack with a count of 1 as it is the first instance
            else:
                stack.append([char, 1])

            # Then, check if the count of current char equals the value of k
            # If true, pop from the top of stack
            if stack[-1][1] == k:
                stack.pop()

        # Initialize ans as empty string to put non-duplicated string from stack
        # For every char, put into the ans string for 'count' times and return ans
        ans = ""
        for char, count in stack:
            ans += (char * count)
        return ans


