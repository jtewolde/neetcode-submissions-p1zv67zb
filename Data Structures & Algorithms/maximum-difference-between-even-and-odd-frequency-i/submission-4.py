class Solution:
    def maxDifference(self, s: str) -> int:
        # Synposis: Find out all frequencies of letters in the string
        # Take the max freqs of two characters, one odd and one even
        # Take the difference between those two and return it as answer

        count_s = Counter(s)
        max_odd, min_even = 0, len(s)

        for freq in count_s.values():
            if freq % 2 == 1:
                max_odd = max(max_odd, freq)
            else:
                min_even = min(min_even, freq)

        return max_odd - min_even