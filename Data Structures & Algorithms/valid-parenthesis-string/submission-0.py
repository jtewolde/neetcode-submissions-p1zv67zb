class Solution:
    def checkValidString(self, s: str) -> bool:
        # Approach for solving this problem is by using Two Stacks method

        # Synposis: Create two different stacks, left fot tracking left parentheses in string
        # star for tracking star characters in the string
        # Iterate through the string with enumerate, getting the char and the index
        # See if the current char is "(" or a "*", append index of char to corresponding stack
        # Otherwise, the char is a right parenthesis. See if both stacks are empty, return False
        # If not, pop out index from left stack if the left stack has a left parenthesis first to match with right parentheses
        # Else, pop out index from star stack

        # After the for loop: See if there is any leftover left parentheses that can be popped with star wildcard
        # While left and star stack isn't empty, compare popped out index from left and star stacks,
        # If the left.pop > star.pop, return false. 
        # Meaning, if the index of the left parentheses is greater than the star's index, return false as left parentheses can't be popped
        # Finally, return the boolean result if there is no left parenthesis unmatched

        # Initialize stacks for left and star parenthesis
        left = []
        star = []

        # Iterate through string with char and index
        # See if current char is left parenthesis or star, append to respective stack
        for ind, char in enumerate(s):
            if char == '(':
                left.append(ind)
            elif char == '*':
                star.append(ind)
            # If char is a right parenthesis, if there are no stars or left parentheses, return False
            # If there are left parentheses, pop out value from left stack
            # Else, pop from the star stack
            else:
                if not left and not star:
                    return False
                if left:
                    left.pop()
                else:
                    star.pop()

        # If there are any remanining left parentheses and stars
        # See if the index of remaining left is greater than the star, if so, return False
        while left and star:
            if left.pop() > star.pop():
                return False

        # Return boolean for if there are unmatched left parentheses remaining
        return not left










