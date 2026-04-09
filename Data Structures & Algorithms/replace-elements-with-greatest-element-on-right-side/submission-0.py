class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Approach: Use reverse traversal(right-left) to track the maximum value so far and store current maximum at current element
        # Explanation: For each element, replace it with the maximum of all elements to the right of it
        # With this approach, s single pass of the array can be completed for better run time
        
        # First, initialize maxx variable with -1 to track current max value
        # Start with -1 to make last element in arr -1 as default
        maxx = -1
        n = len(arr)

        # Iterate through arr startign from last element using reverse traversal
        for i in range(n - 1, -1, -1):
            # Store original value of current element in temp variable
            # Replace current element with current max
            tempVal = arr[i]
            arr[i] = maxx

            # Update maxx variable to include current element's value
            maxx = max(maxx, tempVal)
        
        return arr