# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

def valid_anagram(data1, data2):
    from collections import Counter
    if len(data1) != len(data2):
        return False
    return sorted(data1) == sorted(data2)
    #return Counter(data1) == Counter(data2)


a = "anagram"
b = "nagaram"
print(valid_anagram(a, b))
