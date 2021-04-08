# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true

def validate_brackets(s):
    if len(s) % 2 != 0:
        return False
    
    a = ['(', '{', '[']
    mapping = {'(' : ')', '{' : '}', '[' : ']'}
    
    stack = []
    
    for i in s:
        if i in a:
            stack.append(i)
        elif stack and i == mapping[stack[-1]]:
            stack.pop()
        else:
            return False
    return stack == []


print(validate_brackets("{()}[]"))