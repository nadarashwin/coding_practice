# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"


def LCP(prefix, word):
    i = 0
    while i < len(prefix) and i < len(word):
        if prefix[i] != word[i]:
            break
        i += 1
    return prefix[:i]


# def findLCP(words):
#     prefix = words[0]
#     for word in words:
#         prefix = LCP(prefix, word)
#     return prefix

def findLCP(words, low, high):
    if low > high:
        return ""

    if low == high:
        return words[low]

    # prefix = words[0]
    # for word in words[1:]:
    #     prefix = findLCP(prefix, word)
    # return prefix
    mid = (low+high) // 2
    print(mid)
    x = findLCP(words, low, mid)
    y = findLCP(words, mid+1, high)

    return LCP(x, y)


words = ["techie delight", "tech", "techie", "technology", "technical"]
# print(findLCP(words))
print(findLCP(words, 0, len(words)-1))
