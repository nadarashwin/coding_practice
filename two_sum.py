# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(nums, target):
    hash_table = {}
    for i, j in enumerate(nums):
        temp = target - j
        if temp not in hash_table:
            hash_table[j] = i
        else:
            return(i, hash_table[temp])
    return("nothing found")

print(two_sum([2,7,11,15], 9))
print(two_sum([3,2,4], 6))
print(two_sum([3,3], 6))