# Find the missing number in an array
# Given an array of n-1 distinct integers in the range of 1 to n, find the missing number in it in linear time.

# For example, consider array {1, 2, 3, 4, 5, 7, 8, 9, 10} whose elements are distinct and within the range of 1 to 10. The missing number is 6.


def missing_number(data):
    # # ---> The Gaus Law
    # # data1 - to add numbers, we could have used sum too for adding
    # data1 = len(data) * (data[0] + data[-1]) // 2
    # data2 = sum(list(range(data[0], data[-1]+1)))
    # return (data2 - data1)

    # # ---> The SUM way
    # sum1 = sum(data)
    # sum2 = sum(list(range(data[0], data[-1]+1)))
    # return (sum2 - sum1)

    # ---> The XOR way
    xor = 0
    # Compute XOR of all the elements in the list
    for i in data:
        xor ^= i

    # Compute XOR of all the elements from 1 to 'n+1'
    # (len(data) + 1 + 1) -> first '+ 1' is to iterate through the entire
    # length and the second '+ 1' is for the missing number
    for i in range(1, len(data) + 1 + 1):
        xor ^= i

    return xor


print(missing_number([1, 2, 3, 4, 7, 8, 9, 10]))
