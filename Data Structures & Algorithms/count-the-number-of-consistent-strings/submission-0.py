class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Approach: Use iteration and hashset to see if characters in current word is in the allowed string
        # Initialize consistent variable that stores number of consistent strings(words that have chars from allowed)
        # Also, use a hashset on allowed string to count frequencies of each char in allowed
        # Iterate through every word in words array
        # Create boolean variable that determines if current word is consistent(chars are in allowed string)
        # Make another for loop that iterates through every character in current word
        # If the char isn't in the set, change boolean variable to false and break from char loop
        # Otherwise, if all chars in current word are in the set, increment consistent by one
        # Return consistent as final answer
        
        # Initialize consistent variable that stores number of consistent strings(words that have chars from allowed)
        # Also, use a hashset on allowed string to count frequencies of each char in allowed
        consistent = 0
        allowed_set = set(allowed)

        # Iterate through every word in words array
        # Create boolean variable that determines if current word is consistent(chars are in allowed string)
        for word in words:
            isConsistent = True

            # Make another for loop that iterates through every character in current word
            for char in word:
                # If the char isn't in the set, change boolean variable to false and break from char loop
                if char not in allowed_set:
                    isConsistent = False
                    break
            
            # Otherwise, if all chars in current word are in the set, increment consistent by one
            if isConsistent == True:
                consistent += 1

        # Return consistent as final answer
        return consistent

            