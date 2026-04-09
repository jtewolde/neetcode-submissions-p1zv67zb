class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Approach: Use two pointers techinque to iterate through both greed and cookies array
        # Compare the current greed element of a child to the size of cookie with pointers
        # If the cookie element is greater than greed element, increment ans variable and move greed pointer to next child
        # Regardless, move cookie pointer forward

        # Sort both greed and cookies array for easier iteration
        g.sort()
        s.sort()

        # Create both pointers for greed and cookie arrays, starting at zero
        i = j = 0
        ans = 0

        # Iterate through both greed and cookie arrays using both pointers
        while i < len(g) and j < len(s):

            # If size of cookie element is greater than or equal to greed, then move pointer for cookie array
            # Increment ans variable for final answer
            if s[j] >= g[i]:
                i += 1
                ans += 1
            # Move on to next cookie
            j += 1

        return ans
