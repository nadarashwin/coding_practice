# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

# Example 1:

# Input: x = 121
# Output: true



def palindrome_no(data):
    if data < 0 :
        return False

    temp = data
    reminder = 0

    while temp > 0:
        index = temp % 10
        reminder = reminder * 10 + index
        temp = temp // 10

    if reminder == data:
        return True
    return False

    # if str(data) == str(data)[::-1]:
    #     return True
    # return False

raw = -121
print(palindrome_no(raw))