# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.


# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Nice explaination -> https://leetcode.com/problems/merge-intervals/discuss/21227/7-lines-easy-Python


def merge_intervals(data):
    temp_array = []
    for i in sorted(data): # for i in sorted(data, key=lambda x: x[0])
        if temp_array and i[0] <= temp_array[-1][-1]:
            temp_array[-1][-1] = max(i[-1], temp_array[-1][-1])
        else:
            temp_array += i, # comma is equivalent to appending -> temp_array += [i] OR temp_array.append(i)
    return temp_array


# a = [[1,4],[2,3]]
a = [[1, 3], [8, 10], [2, 6], [15, 18]]
print(merge_intervals(a))
