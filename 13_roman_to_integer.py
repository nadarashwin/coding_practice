# Given a roman numeral, convert it to an integer.

# Example 1:

# Input: s = "III"
# Output: 3


values = {
  "I": 1,
  "V": 5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000,
}


def rom_to_int(roman):
    """
    i = 0
    total = 0

    while i < len(roman):
        first_param = values[roman[i]]
        if (i +1) < len(roman):
            second_param = values[roman[i+1]]
            if first_param < second_param:
                total = total - first_param
                i += 1
            else:
                total = total + second_param
                i += 1
        else:
            total = total + first_param
            i += 1
    return total

    """
    # Initialize previous character and answer

    p = 0
    ans = 0
    for i in range(len(roman) - 1, -1, -1):
        if values[roman[i]] >= p:
            ans += values[roman[i]]
        else:
            ans -= values[roman[i]]
        p = values[roman[i]]

    return ans


print(rom_to_int('V'))
print(rom_to_int('IV'))
print(rom_to_int('MCMIV'))
