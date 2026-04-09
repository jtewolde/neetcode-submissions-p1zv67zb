class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Approach: Use two hashmaps to map characters in s string to t string as one for one mapping
        # Iterate through both string at the same time
        # Make sure that both current chars in loop are mapped to each other in both maps
        # If not, then return false. If mapped correctly, map current chars to each other in both dictionaires

        # Initialize two hashmaps/dictionaires for bidirectional mapping of s and t characters
        map_ST = {}
        map_TS = {}

        # Iterate through both strings with length of s string as they have same length
        for i in range(len(s)):
            sChar, tChar = s[i], t[i] # Get chars from both strings at current index
  
            # Make sure that current chars in both strings are mapped to each other in both maps
            # If one char isn't mapped to the other map, then return false
            if ((sChar in map_ST and map_ST[sChar] != tChar) or
            (tChar in map_TS and map_TS[tChar] != sChar)):
                return False

            # If other chars are mapped correctly, then map current chars to each other
            map_ST[sChar] = tChar
            map_TS[tChar] = sChar

        # By default, return true, expecting all chars have been mapped to each other
        # And the string is isomorphic
        return True



