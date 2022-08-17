# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2


def get_index_for_first_match(haystack, needle):
    if len(needle) == 0:
        return 0
    if len(haystack) < len(needle):
        return -1
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1


print(get_index_for_first_match("hello", "ll"))
