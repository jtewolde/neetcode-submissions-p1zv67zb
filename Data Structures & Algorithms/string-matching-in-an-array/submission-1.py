class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # Brute Force: Use nested for loops for find out if string is a substring of other strs
        # First loop is for setting the current substring
        # Second loop is for comparing substring to other strings in array
        # First, sort the words array based on length 
        # If the current string is in another string, append the string into the ans array

        # Initialize ans array that stores substrings and sort words array based on length
        ans = []
        words.sort(key=len)

        # Create nested for loop that compares current string at index i to string at index j 
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                # If i-string is in j-string, then append to ans array as substring
                # Break from loop to prevent multiple duplicate answers
                if words[i] in words[j]:
                    ans.append(words[i])
                    break

        return ans
