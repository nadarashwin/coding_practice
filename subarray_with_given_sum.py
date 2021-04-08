# Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

# Example 1:

# Input:
# N = 5, S = 12
# A[] = {1,2,3,7,5}
# Output: 2 4
# Explanation: The sum of elements 
# from 2nd position to 4th position 
# is 12.




def subarray_with_given_sum(data, target):
    for i in range(len(a)):
        sum_tmp = 0
        for j in range(i, len(a)):
            sum_tmp += a[j]
            if sum_tmp == s:
                print(a[i:j+1])
    return


a = [1,2,3,7,5]
s = 12

print(subarray_with_given_sum(a, s))