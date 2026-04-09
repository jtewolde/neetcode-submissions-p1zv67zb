class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Initial Approach: Use Counter on both "Balloon" string 
        # and text string to get count for each character.
        # Loop through each character in "balloon" string,
        # For each character in text string, find out the ratio between available text and required text
        # The ratio will determine how many instances of balloon can be formed from text string
        # Take the minimum ratio for each character and updae ans

        # Initiallize hashmaps/counters for both text string and "balloon"
        # And ans variable to keep track of number of times balloon can be formed from text string
        balloonText = Counter("balloon")
        textCount = Counter(text)
        ans = len(text)

        # Iterate through each character in balloon counter
        # Update ans with the minimum ratio between available chars in text and required from balloon
        for char in balloonText:
            ans = min(ans, textCount[char] // balloonText[char])
        return ans

