class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # Approach: Use Two pointers to iterate through both word and abbr variables
        # First, initialize both pointers for traversing through both word and abbr strings
        # Create while loop that executes until both pointers reach end of their variable strings
        # Compare both elements at pointers if abbr[j] is a character, check if both are the same
        # If true, increment both pointers forward
        # Other case, if abbr[j] is a number, determine if the number is multi-digit
        # If multi-digit, build the complete number by collecting consecutive digits
        # Then, skip the word pointer based on that number
        # Return the result if both pointers reach the end of their strings

        # First, initialize both pointers for traversing through both word and abbr strings
        wordPointer = abbrPointer = 0

        # Create while loop that executes until both pointers reach end of their variable strings
        while wordPointer < len(word) and abbrPointer < len(abbr):
            # If abbr is a leading zero, automatically return as false
            if abbr[abbrPointer] == '0':
                return False
            
            # Compare both elements at pointers if abbr[j] is a character, 
            # Check if both are the same
            if abbr[abbrPointer] == word[wordPointer]:
                wordPointer += 1
                abbrPointer += 1
            elif abbr[abbrPointer].isalpha():
                return False

            # Other case, if abbr[j] is a number, determine if the number is multi-digit
            else:
                # Initialize variable to hold count of number of letters to skip in word
                skipWordCount = 0

                # If multi-digit, build the complete number by collecting consecutive digits
                while abbrPointer < len(abbr) and abbr[abbrPointer].isdigit():
                    skipWordCount = skipWordCount * 10 + int(abbr[abbrPointer])
                    abbrPointer += 1

                # Skip number of letters in word
                wordPointer += skipWordCount

        # Return the result if both pointers reach the end of their strings
        return wordPointer == len(word) and abbrPointer == len(abbr)
                

            

