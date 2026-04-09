class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Approach to solving this problem is by using DP and Bottom-Up DP programming
        # Goal: See if portions/all of string s is in any words in wordDict
        # dp[i] represents whether the substring s[0:i] can be divided into words from wordDict
        # Base case: dp[len(s)] = True since reaching end of string means that string s can be broken down to words that are in dict
        
        # First, initialize dp array where each value in array is false except of len(s)
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        # Create for loop that goes reverse, starting at len(s) to beginning of string s
        for indx in range(len(s) - 1, -1, -1):
            # Then, Iterate through every word in dictionary
            for word in wordDict:
                # See if the current index, i, + length of current word is <= length of string, meaning that word segment within the string
                # And if the word segment starting at curr index to index + length of curr word equals the current word
                if(indx + len(word) <= len(s) and s[indx: indx + len(word)] == word):
                    dp[indx] = dp[indx + len(word)]
                # If both are true: then set dp[i] = dp[i + len(w)]
                # Finally, see if current dp[val] == true, skip it by usign break
                if dp[indx]:
                    break

        return dp[0]