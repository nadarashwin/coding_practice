# How to check if an integer is even or odd?

def odd_or_even(data):
    # if (data & 1) == 0:
    #     return 'even'
    # else:
    #     return 'odd'

    if data % 2 == 0:
        return 'even'
    else:
        return 'odd'

a = 8
print(odd_or_even(a))