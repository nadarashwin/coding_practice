# How to check if a number is a power of 2
# The algorithm needs to be:

# Simple
# Correct for any ulong value.

# https://stackoverflow.com/a/600306/5894668

def power_of_2(data):
    return (data != 0) and (data & (data - 1) == 0)

a = 6
print(power_of_2(a))