# Given a string S, return the "reversed" string where all characters
# that are not a letter stay in the same place, and all letters reverse their positions.

# Example 1:

# Input: "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:

# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"


def reverse_string1(data):
    # ------FIRST WAY------
    # tmp = [r for r in data if r.isalpha()]
    # arr = []
    # for i in data:
    #     if i.isalpha():
    #         arr.append(tmp.pop())
    #     else:
    #         arr.append(i)
    # return tmp, ''.join(arr)

    # ------SECOND WAY------
    data = list(data)
    left, right = 0, len(data) - 1

    while left < right:
        if not (data[left].isalpha()):
            left += 1
        elif not (data[right].isalpha()):
            right -= 1
        else:
            data[left], data[right] = data[right], data[left]
            left += 1
            right -= 1

    return ''.join(data)


a = "7_28]"
a = "a-bC-dEf-ghIj"
print(reverse_string1(a))
