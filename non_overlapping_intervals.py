# Given an array of intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
# Example 2:

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
# Example 3:

# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

# Nice explaination -> https://leetcode.com/problems/non-overlapping-intervals/discuss/91721/Short-Ruby-and-Python


def non_overlapping_interval(data):
    end = float('-inf') # Negative Infiinity
    erased = [] # erased = 0 // you can return either the interval or the number of intervals.
    for i in sorted(data, key=lambda x: x[-1]):
        if i[0] >= end: # store the first interval's end and then compare the same with the first element of next interval
            end = i[-1]
        else:
            erased += i, # erased += 1
    return erased


#a = [[1,2],[2,3],[3,4],[1,3]]
#a = [[1,2],[1,2],[1,2]]
a = [[1,2],[2,3]]
print(non_overlapping_interval(a))