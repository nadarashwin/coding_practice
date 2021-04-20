# Given an array arr[] of integers, find out the maximum difference between any two 
# elements such that larger element appears after the smaller number. 

# Examples :  

# Input : arr = [2, 3, 10, 6, 4, 8, 1]
# Output : 8
# Explanation : The maximum difference is between 10 and 2.

# Input : arr = [7, 9, 5, 6, 3, 2]
# Output : 2
# Explanation : The maximum difference is between 9 and 7.

def max_diff(data):
    # Time Complexity : O(n^2) 
    # maxDiff = float('-inf') # Negative infinity || data[1] - data[0]
    # for i in range(len(data)):
    #     for j in range(i+1, len(data)):
    #         maxDiff = max(maxDiff, (data[j] - data[i]))
    # return maxDiff

    # Time Complexity : O(n) 
    maxDiff = float('-inf')
    max_so_far = data[-1]
    for i in reversed(data): # traverse the list from the right and keep track of the maximum element
        if i > max_so_far:
            max_so_far  = i
        else:
            maxDiff = max(maxDiff, (max_so_far - i))

    return maxDiff

# a = [2, 7, 9, 5, 1, 3, 5]
# a = [1, 2, 90, 10, 110]
a = [80, 2, 6, 3, 100]
print(max_diff(a))