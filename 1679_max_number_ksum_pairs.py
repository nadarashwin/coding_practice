# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.

# Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.

# Nice explaination -> https://leetcode.com/problems/max-number-of-k-sum-pairs/discuss/1022699/Python-Short-Counter-solution-%2B-Oneliner-explained


def maxOperations(data, k):
    from collections import Counter
    count, maxO = Counter(data), 0
    print(count)
    for val in count:
        maxO += min(count[val], count[k - val]) # if a key isn't present in Counter, it returns 0
        print(maxO, count[val], count[k-val])
    return maxO//2

    # from collections import defaultdict
    # s = defaultdict(set)
    # max_p = 0
    # for i, j in enumerate(data):
    #     tmp = k - j
    #     if tmp not in s or len(s[tmp]) == 0:
    #         s[j].add(i)
    #     elif len(s[tmp]) > 0:
    #         s[tmp].pop()
    #         max_p += 1

    # return max_p

# nums = [1,2,3,4]
# k = 5


nums = [3,1,3,4,3]
k = 6

print(maxOperations(nums, k))
