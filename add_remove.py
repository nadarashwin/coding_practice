# Insert Delete GetRandom O(1) - Duplicates allowed

# Example 1:

# Input
# ["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
# [[], [1], [1], [2], [], [1], []]
# Output
# [null, true, false, true, 2, true, 1]


from collections import defaultdict
from random import choice

class toggle:
    def __init__(self):
        self.lst = [] # Create a empty list 
        self.dict =  defaultdict(set) # create dict with set as the  default dict as duplicates are allowed
        
    def insert(self, val):
        # set allows add method wherein list allows append
        self.dict[val].add(len(self.lst)) # length is less than the index 
        self.lst.append(val)
        print(self.lst,  self.dict)
        return len(self.dict[val]) == 1

    def remove(self, val):
        if val not in self.dict or len(self.dict[val]) == 0:  # we don't remove key from dict ONLY remove the index value
            return False

        idx = self.dict[val].pop() # get the index of the value passed from the dict
        # cannot use pop for lst directly, can cause idx out of range issue if it's the last one
        last = self.lst[-1]

        self.dict[last].add(idx) # add the index of the value to be removed to the last element in the dict
        self.lst[idx] = last  # replace the value of the index to be removed with last

        self.dict[last].remove(len(self.lst) - 1) # remove the old index  of last
        print(self.lst,  self.dict)
        self.lst.pop()
        return True

    def getRandom(self):
        return choice(self.lst)


a = toggle()
# print(a.insert(2))
# print(a.insert(24))
# print(a.insert(22))
# print(a.insert(21))
# print(a.remove(2))
## ------------------- ##
print(a.insert(1))
print(a.remove(1))
print(a.insert(1))
print(a.getRandom())