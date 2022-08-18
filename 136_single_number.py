# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?


# Example 1:

# Input: nums = [2,2,1]
# Output: 1


def single_number(number):
    result = 0
    for element in number:
        # If the two arguments are the same, the result is always 0
        result ^= element
    return result

    # temp_list = []
    # for element in number:
    #     if element not in temp_list:
    #         temp_list.append(element)
    #     else:
    #         temp_list.remove(element)
    # return temp_list.pop()


print(single_number([2,2,1]))
print(single_number([4,1,2,1,2]))
print(single_number([1,5,3,4,5,1]))
