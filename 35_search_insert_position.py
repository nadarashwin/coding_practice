# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4


def searchInsert(nums, target):
    for i in range(len(nums)):
        # print(nums[i], target)
        if nums[i] >= target:
            return i
    return len(nums)


print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 7))
