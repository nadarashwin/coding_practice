# Given an unsorted array of nonnegative integers, find a continuous subarray which adds to a given number. 
# Examples : 

# Input: arr[] = [1, 4, 20, 3, 10, 5], sum = 33
# Ouptut: Sum found between indexes 2 and 4
# Sum of elements between indices
# 2 and 4 is 20 + 3 + 10 = 33

# Input: arr[] = [1, 4, 0, 0, 3, 10, 5], sum = 7
# Ouptut: Sum found between indexes 1 and 4
# Sum of elements between indices
# 1 and 4 is 4 + 0 + 0 + 3 = 7

# Input: arr[] = [1, 4], sum = 0
# Output: No subarray found
# There is no subarray with 0 sum


def subarray_with_given_sum(data, target):
    for i in range(len(a)):
        sum_tmp = 0
        for j in range(i, len(a)):
            sum_tmp += a[j]
            if sum_tmp == s:
                #return(a[i:j+1])
                return (i,j)
    return


a = [1, 4, 20, 3, 10, 5]
s = 33

print(subarray_with_given_sum(a, s))