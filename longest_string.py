# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def longest_string(data):
    start = maxL = 0
    temp = {}
    for index in range(len(data)):
        if data[index] in temp and temp[data[index]] >= start:
            start = temp[data[index]] + 1
        temp[data[index]] = index
        maxL = max(maxL, index - start + 1)
    #print(start, maxL)

    return maxL

print(longest_string("abcabcbbd"))
print(longest_string("bbbbb"))
print(longest_string("pwwkew"))
print(longest_string("abc"))
print(longest_string(""))
print(longest_string(" "))
print(longest_string("abcabcbb"))
print(longest_string("abba"))