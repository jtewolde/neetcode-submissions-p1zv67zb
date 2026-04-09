class Solution:
    def maxDifference(self, s: str) -> int:
        # Synposis: Find out all frequencies of letters in the string
        # Take the max freqs of two characters, one odd and one even
        # Take the difference between those two and return it as answer

        # Initialize Counter for getting freqs of each char in string
        # maxOdd and minEven variables for getting the max freq of odd chars and getting min of even characters
        count_s = Counter(s)
        max_odd, min_even = 0, len(s)

        # Go through the frequencies of each character in the string
        for freq in count_s.values():
            # Determine if freq of current character is odd or even using mod division
            # Update maxOdd or minEven based on it
            if freq % 2 == 1:
                max_odd = max(max_odd, freq)
            else:
                min_even = min(min_even, freq)

        # Get the difference between the two variables and return it
        return max_odd - min_even