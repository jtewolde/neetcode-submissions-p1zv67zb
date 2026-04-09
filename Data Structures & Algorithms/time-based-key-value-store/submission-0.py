class TimeMap:
    # Approach to solve this problem is by using hashtable to store key-value pairs
    # Where the key is the string word and the value is an array with the value and timestamp
    # Synposis: Init function is to create a self variable that uses hashmap to store k-v
    # Set function is simple where if the desired key isn't in the self.kvs, create a new key-value where value of key is empty array
    # Else, make the value of created key to be an array that has [val, timestamp]

    def __init__(self):
        # Initialize hashtable for time-based key value store
        self.kvs = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:

        # Check if the given key isn't in the key-value store,
        # If not, set the value for given key to empty array
        if key not in self.kvs:
            self.kvs[key] = []
        # Else, set the associated value of given key to array that stores [value, timestamp]
        self.kvs[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:

        # Preinitialize left and right pointers for performing binary search.
        # ans variable to store reesult from get function, 
        ans, values = "", self.kvs.get(key, [])
        left, right = 0, len(values) - 1

        # Perform binary search by finding mid value 
        while left <= right:
            mid = (left + right) // 2

            # If the timestamp of the key is less than desired timestamp from get call
            # Set the ans string to value of said key with largest timestamp less than given timestamp
            # Move the left pointer towards middle to get timestamp closer
            if values[mid][1] <= timestamp:
                ans = values[mid][0]
                left = mid + 1

            # Otherwise, move right pointer inwards and return "" as the desired timestamp
            # Is less than timestamp of desired key from get function call
            else:
                right = mid - 1

        return ans




        
