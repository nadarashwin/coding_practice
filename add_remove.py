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
        if val not in self.dict:
            return False

        idx = self.dict[val].pop() # get the index of the value passed from the dict
        last = self.lst.pop() # pop out the last element from the list

        self.dict[last].add(idx) # add the index of the value to be removed to the last element in the dict
        self.lst[idx] = last  # replace the value of the index to be removed with last

        self.dict[last].remove(len(self.lst)) # remove the old index  of last
        print(self.lst,  self.dict)
        return True

    def getRandom(self):
        return choice(self.lst)


a = toggle()
print(a.insert(2))
print(a.insert(24))
print(a.insert(22))
print(a.insert(21))
print(a.remove(2))
print(a.getRandom())