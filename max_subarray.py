# Given an array arr of N integers.
# Find the contiguous sub-array with maximum sum. (Kadane's Algorithm)

# Example 1:

# Input:
# N = 5
# arr[] = {1,2,3,-2,5}
# Output:
# 9
# Explanation:
# Max subarray sum is 9
# of elements (1, 2, 3, -2, 5) which
# is a contiguous subarray.

def max_subarray(data):

    # Block of code to tackle the issue where all the elments are negative.
    maximum = max(data)
    # if the list contains all negative values, return the maximum element
    if maximum < 0:
        return maximum

    # stores the maximum sum sublist found so far
    maxi = 0

    # stores the maximum sum of sublist ending at the current position
    current = 0

    for element in data:
        current = current + element
        current = max(current, 0)  # if current is negative, set it to 0
        maxi = max(current, maxi)  # update maxi if current sublist is greater
        print(current, maxi)
    return maxi


a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(max_subarray(a))
