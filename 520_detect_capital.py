# We define the usage of capitals in a word to be right when one of the following cases holds:
#
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.
#
# Example 1:
#
# Input: word = "USA"
# Output: true
# Example 2:
#
# Input: word = "FlaG"
# Output: false


def detectCapital(data):
    # return data.isupper() or data.istitle() or data.islower()
    # return len(data) == 1 or data[1:].islower() or data.isupper()
    return data in [data.upper(), data.lower(), data.capitalize()]


print(detectCapital("USA"))
print(detectCapital("FlaG"))
print(detectCapital("leetcode"))
print(detectCapital("Google"))
