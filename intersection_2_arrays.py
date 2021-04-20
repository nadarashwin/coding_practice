# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and
#  you may return the result in any order.


# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

def intersection_2_arrays(data1, data2):
    # from collections import Counter

    # a, b = map(Counter, (data1, data2))
    # """
    # elements() -> Return an iterator over elements repeating each as many times as its count.
    # Elements are returned in the order first encountered.
    # If an element’s count is less than one, elements() will ignore it.
    # """
    # return list((a&b).elements())

    temp_dict = {}
    # block of code that takes care of Counter in collections
    for i in data1:
        if i in temp_dict:
            temp_dict[i] += 1
        else:
            temp_dict[i] = 1

    ret = []
    for i in data2:
        if i in temp_dict and temp_dict[i] > 0: # key remains in the dict, hence we make sure the value > 0
            ret.append(i)
            temp_dict[i] -= 1 # decrement the value for every match

    return ret



nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection_2_arrays(nums1, nums2))