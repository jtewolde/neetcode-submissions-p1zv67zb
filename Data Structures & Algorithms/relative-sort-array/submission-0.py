class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Approrach: Use a hashmap to get the count of each number in arr1 using defaultDict
        # Also, convert arr2 into a set for better time optimization
        # First, iterate through every num in arr1 and increment the count of curr num in arr1 hashmap
        # Check if current num is in arr2, if not, append it to an end array that stores nums that aren't in arr2 to be put at the end of final array
        # Then, sort end array after iteration
        # Finally, create a nested for loop where for every number in arr2 set, 
        # Append that number according to its freq to the ans array
        # Combine both the ans array and end array to get the final ans and return it

        # Initialize arr1Count hashmap for getting count of each number in arr1, convert arr2 into set
        # Then, create end array that stores all nums that aren't in arr2 sorted and ans for all nums using count
        arr1Count = defaultdict(int)
        arr2Set = set(arr2)
        end = []
        ans = []

        # Iterate through every num in arr1 and check if current num is or isn't in arr2 set
        # If not, append it onto the end array. Regardless, increase count of current num in arr2
        for num in arr1:
            if num not in arr2Set:
                end.append(num)
            arr1Count[num] += 1

        # Sort the end array that stores extra elements not in arr2
        end.sort()

        # Build the ans array where for each num in arr2, 
        # Append it to the ans array as many times it appears in arr1
        for num in arr2:
            for _ in range(arr1Count[num]):
                ans.append(num)
        # Append the end array to the end of ans and return as final answer
        return ans + end




