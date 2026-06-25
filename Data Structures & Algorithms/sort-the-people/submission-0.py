class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Approach: Use a hashmap/dictionary to associate a name to the height based on index
        # Then, sort the heights array in ascending order,
        # Iterate through all of the heights in reverse
        # For every height encountered, look up the mapped name in the hash map and append to final ans
        # Return final ans array as final answer

        # Initialize hashmap to map names to associated heights
        # Also, create ans array that will store final order of names in descending order
        height_to_name = {}
        ans = []

        # Iterate through both heights and names array simultaneously to map each height with a name
        for height, name in zip(heights, names):
            height_to_name[height] = name

        # Sort the original heights array in reverse order.
        # Then, iterate through each height in the array and append the associated name to the ans array
        heights.sort(reverse=True)   
        for h in heights:
            ans.append(height_to_name[h])

        return ans