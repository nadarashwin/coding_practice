# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.
#
# Example 1:
#
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
#
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


def majorityElement(nums):
    # ------FIRST WAY------
    # Majority elements always exist and appears more than [n/2]
    # nums.sort()
    # return nums[len(nums)//2]

    # ------SECOND WAY------
    # Boyer-Moore Voting Algorithm
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            # Consider first element is the majority element
            candidate = num
            # we maintain a count, which is incremented whenever we see an
            # instance of our current candidate for majority element and
            # decremented whenever we see anything else
            # Whenever count equals 0, we effectively forget about everything
            # in nums up to the current index and consider the current number
            # as the candidate for majority element
        if candidate == num:
            count += 1
        else:
            count -= 1
    return candidate

    # ------THIRD WAY------
    # from collections import Counter
    # nums = Counter(nums)
    # return next(iter(nums))


print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))
