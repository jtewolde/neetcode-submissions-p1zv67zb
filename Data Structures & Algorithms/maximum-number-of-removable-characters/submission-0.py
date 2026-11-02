class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        # Problem: Determine if string p is still a subsequence of string s after removing chars at indexes from removable array in string s
        # Approach: Use binary search and iteration to check if a subsequece was found in the given string with helper function
        # Then, apply binary search on removable array and hashset to find the maxinum num of removable chars

        # Create helper function to determine if given strings are a subsequence of another
        def isSubseq(s, subseq):
            idx1, idx2 = 0, 0

            # Iterate through both given string and subseq string and determine if the given string is a subsequence of another
            while idx1 < len(s) and idx2 < len(subseq):
                # If the current char at idx1 is already removed or both characters don't match, then move onto next char from string
                if idx1 in removed or s[idx1] != subseq[idx2]:
                    idx1 += 1
                    continue
                # Otherwise, both chars are the same and move onto next char in both strings
                idx1 += 1
                idx2 += 1
            return idx2 == len(subseq)
        
        # Create ans array to store max num of removable chars and left/right pointers for binary search
        ans = 0
        left, right = 0, len(removable) - 1

        # Apply binary search to find the max removable chars using given strings s and p
        while left <= right:
            mid = (left + right) // 2

            # Create removed hashset to store chars that have been removed and add chars 
            removed = set(removable[:mid + 1])
            if isSubseq(s, p):
                ans = max(ans, mid + 1)
                left = mid + 1
            else:
                right = mid - 1
        return ans











