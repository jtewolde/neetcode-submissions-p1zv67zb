class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Approach: Use a Counter data structure to track the frequencies of all strings in arr
        # Iterate through key items in Counter
        # If encountering string that has freq of 1, then decrement k variable to count distinct element
        # If/When k variable reaches zero, return the string
        # Otherwise, return empty string if k doesn't reach zero after iteration
        
        # Initialize Counter hash map that shows the frequency of each string in arr
        count = Counter(arr)

        # Iterate through each element and freq in Counter key items
        for element, freq in count.items():
            # If frequency of element is one, decrement k as it is a distinct element
            if freq == 1:
                k -= 1
                # If value of k is zero, then return last distinct element
                if k == 0:
                    return element

        # After iteration, if k is nozero, return empty string 
        return ""