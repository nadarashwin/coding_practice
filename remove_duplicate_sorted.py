# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2]
# Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. 
# It doesn't matter what you leave beyond the returned length.




# def removeSortedList(data):
#     ## inPlace
#     data[:] =  sorted(set(data)) ## The difference between nums[:] = and nums = is that the latter doesn't replace elements in the original list.
#     return data

def removeSortedList(data):
    ## inPlace
    counter = 0
    while (counter < len(data)):
        if data[counter] in data[:counter]:
            del data[counter]
        else:
            counter += 1
    return data

print(removeSortedList([1,1,2]))
print(removeSortedList([-1,0,0,0,0,3,3]))