class MyHashSet:

    # Initialize self.hset variable to use list data structure for hashset
    def __init__(self):
        self.hset = []      

    # Add function that checks if key is already in hset, if not, add to hset
    def add(self, key: int) -> None:
        if key not in self.hset:
            self.hset.append(key)

    # Remove function that checks if key is in hset, then remove key from array
    def remove(self, key: int) -> None:
        if key in self.hset:
            self.hset.remove(key)
    
    # Contains function that checks if current key is in hset, return boolean
    def contains(self, key: int) -> bool:
        if key in self.hset:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)