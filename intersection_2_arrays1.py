# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

def intersection_2_arrays1(data1, data2):
    # set -> intersection performed using & operator
    #return list(set(data1) & set(data2)) # list(set(nums1).intersection(set(nums2)))

    # brute force
    temp_arr = []
    for i in data1:
        if i not in temp_arr and i in data2:
            temp_arr.append(i)

    return temp_arr

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
# nums1 = [1,2,2,1]
# nums2 = [2,2]
print(intersection_2_arrays1(nums1, nums2))