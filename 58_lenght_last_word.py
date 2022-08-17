# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.


def lengthOfLastWord(data):
    # a = data.split()
    # if not len(a):
    #     return 0
    # return len(a[-1])
    return len(data.rstrip().split()[-1])


print(lengthOfLastWord("hello World"))
print(lengthOfLastWord("    fly me to   the moon    "))
print(lengthOfLastWord("luffy is still joyboy"))
