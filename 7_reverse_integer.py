# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


# Example 1:

# Input: x = 123
# Output: 321


def reverse_integer(data):
    if data <= -2**31 or data >= 2**31-1:
        return 0
    champa = False
    if data < 0:
        champa = True
        data = -data
    reminder = 0
    while data > 0:
        temp = data % 10
        reminder = reminder * 10 + temp
        print(temp)
        data = data // 10
    if champa:
        reminder = -reminder
    return reminder


print(reverse_integer(234))
print(reverse_integer(-234))
