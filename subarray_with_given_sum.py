# Given an array of integers nums and an integer k,
# return the total number of continuous subarrays whose sum equals to k.

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

# Explaination -> https://leetcode.com/problems/subarray-sum-equals-k/discuss/341399/Python-clear-explanation-with-code-and-example


def subarray_with_given_sum(data, target):
    # Brute force way
    # res = 0
    # for i in range(len(a)):
    #     sum_tmp = 0
    #     for j in range(i, len(a)):
    #         sum_tmp += a[j]
    #         if sum_tmp == s:
    #             #print(a[i:j+1])
    #             #print (i,j)
    #             res += 1
    # return res

    # Optimized way -> explaination at the bottom
    d = {}
    d[0] = 1
    count = sums = 0
    for i in data:
        sums += i
        # print('sums ', sums)
        # print('difference ', (sums - target))
        count += d.get(sums - target, 0) # if the difference is present in the dict, increment the count
        # print('count ', count)
        d[sums] = d.get(sums, 0) + 1

    return count


# a = [1, 4, 20, 3, 10, 5]
# s = 33

# a = [ 10, 2, -2, -20, 10 ]
# s = -10

a = [1,2,1,2,1]
s = 3

print(subarray_with_given_sum(a, s))


#  Input -> [1, 2, 1, 2, 1]
#  Hash -> 0 1  3  4  6  7  -> (Prefix Sum)(Hash key)
#          1 1  1  1  1  1  -> Hash value indicating the occurence of key


#            ----
#         ----
#         1  2  1  2  1
#               ----
#                  ----      --> 4 occurences that sum up to 3