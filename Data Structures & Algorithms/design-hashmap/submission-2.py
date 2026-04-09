class MyHashMap:

    # First Approach: Use a list data structure to store key-value pairs
    def __init__(self):
        # Initialize hmap self list that has all keys has -1  for 100000 indexex
        self.hmap = [-1] * 1000001

    # Add new key-value pair to list by using key as index and adding value
    def put(self, key: int, value: int) -> None:
        self.hmap[key] = value

    # Return value from associated key
    def get(self, key: int) -> int:
        return self.hmap[key]
    
    # Remove key-value pair from hashmap by making value back to -1
    def remove(self, key: int) -> None:
        self.hmap[key] = -1
    
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)