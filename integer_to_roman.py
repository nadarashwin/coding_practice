# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# Example 1:

# Input: num = 3
# Output: "III"
# Example 2:

# Input: num = 4
# Output: "IV"

## Good discussion -> https://leetcode.com/problems/integer-to-roman/discuss/6304/Python-simple-solution


def integer_to_roman(data):
    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    integer = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    value = ''
    i = 0
    # while data:
    #     value += (data//integer[i]) *  roman[i]
    #     data %= integer[i]
    #     i += 1
    # return value

    for i, j in enumerate(integer):
        value += (data//j) * roman[i]
        data %= j
    return value

a = 3
print(integer_to_roman(a))