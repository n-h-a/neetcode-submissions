class LRUCache:
    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        for i, pair in enumerate(self.cache):
            if pair[0] == key:
                removed = self.cache.pop(i)
                self.cache.append(removed)
                return pair[1]
        return -1
        
    def put(self, key: int, value: int) -> None:
        for i, pair in enumerate(self.cache):
            if pair[0] == key:
                self.cache.pop(i)
                self.cache.append((key, value))
                return
            
        if len(self.cache) == self.capacity:
            self.cache.pop(0)
        self.cache.append((key, value))


# GOAL
# =======
# Implement an LRU cache s.t.
#   * LRUCache() initializes capacity
#   * get() returns the value corresponding to key if exists. 
#       -1 otherwise.
#   * put() updates the value of key if exists. 
#       Adds to cache otherwise. If exceeds capacity, remove
#       least recently used key.
# Want O(1) avg. TC for get and put.

# BRUTE FORCE
# =======
#   * LRUCache(): Initialize a list of size capacity.
#   * get(): Loop through list to find the key.
#       If found, remove it from current position.
#       Append it to the end and return its value.
#   * put(): Loop through list to find the key.
#       If found, update the value.
#       Othwerise, add to cache if capacity not exceeded.
#           If capacity exceeded, remove end of list and add
#           new pair.
# TC: O(N)
# SC: O(N)
        
