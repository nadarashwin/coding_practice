# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache.
# If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# Follow up:
# Could you do get and put in O(1) time complexity?

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]


from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.od = OrderedDict()
        self.cap = capacity

    def get(self, key):
        if key not in  self.od:
            return -1
        self.od.move_to_end(key) # move_to_end is a method that moves the key to end
        return self.od[key]

    def put(self, key, value):
        self.od[key] = value # create/update key
        self.od.move_to_end(key)

        if len(self.od) > self.cap:
            self.od.popitem(last=False) # popitem method removes the last key by default


a = LRUCache(2)
a.put(*[1,1])
a.put(2,2)
print(a.get(1))
a.put(3,3)
print(a.get(2))
a.put(4,4)
print(a.get(1))
print(a.get(3))
print(a.get(4))