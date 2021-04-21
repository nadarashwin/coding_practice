# Reverse string in Python.

def reverse_string(data):
    ## First way
    #return data[::-1]

    ## Second way
    # dump = ''
    # for i in data:
    #     dump = i + dump
    # return dump

    ## Third way (Optimized way) iterate through only half of the string
    data = list(data)
    left, right = 0, len(data) -1
    while left < right:
        data[left], data[right] = data[right], data[left]
        left += 1; right -= 1

    return ''.join(data)

s = "champesh"
print(reverse_string(s))