class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Basic Understanding of solving problem with bucket sort

        1. Use a hash map to count all of the occurences in nums array
        2. Create a nested array, freq, that keeps track of all of the different numbers
        based off of the # of how many times it appears in nums
        3. First, iterate through nums to get the count of each number and store in
        in the hash map where it adds one 
        4. Then, iterate through key-value pairs in hash map and append the number of times
        a number appears in the nums array(freq[cnt].append(num))
        5. Create a results array to store the numbers that show up k amount of times in nums array
        6. Iterate through the length of frequency array in descending order(most to least)
        7. Then, iterate through freq array, add the numbers in the freq array k amount of times
        8. return result

        """

        count = {} # Hash map
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, c in count.items():
            freq[c].append(num)

        res = []

        for i in range(len(freq) - 1, 0 , -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res










