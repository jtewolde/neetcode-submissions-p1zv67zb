class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # Problem: Given the value of k and the given binary string, determine if every binary code of length k is a substring of s
        # Approach: Create a hashset that will store the binary codes encountered in string iteration.
        # Use a sliding window techinque to get the window of binary nums with size k and iterate through
        # Add the current window into the hashset and continue
        # Return the boolean result if the lenf of the hashet equals with 2^k, which would be the number of binary code generated with length k

        # Initialize hashset that will store binary codes with length k encoutnered in string iteration
        codeSet = set()

        # Iterate through each starting index in string with valid k windows
        for indx in range(len(s) - k + 1):
            # Add the current window of binary strings into the set from indx to indx + k non inclusive
            codeSet.add(s[indx: indx + k])
        # Return the boolean result of comparing length of codeSet to expected num of binary strings created with length k
        return len(codeSet) == 2 ** k


