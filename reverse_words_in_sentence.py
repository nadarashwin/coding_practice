# Reverse words of a sentence.
# For example, if you are given input ‘you shall not pass’, it should return ‘pass not shall you’.

# As a bonus challenge, the program should take care of punctuations.
# (Punctuations should appear in the same order as in the original sentence).
# For example — ‘you, shall not pass!’ should result in ‘pass, shall not you!’


def reverse_words(data):
    import re
    punc = ":;,.?!"
    # Square bracket [] is needed for a single character match with an OR condition.
    # For ex., [:;,.!?] is same as :|;|,|.|!|?
    ot = re.findall(r"\w+|[.,;?!]", data)  # \w	alphanumeric: [0-9a-zA-Z_]

    left = 0
    right = len(ot) - 1

    while left < right:
        # Block of code that will check for a special character and shift one to either left or right
        if (ot[left] in punc):
            left += 1
        elif (ot[right] in punc):
            right -= 1
        else:
            ot[left], ot[right] = ot[right], ot[left]
            left += 1
            right -= 1

    r = ''
    for i in ot:
        if i in punc or len(r) == 0:
            r += i
        else:
            r += ' ' + i
    return ot, r


o = 'you, shall not pass!!'

print(reverse_words(o))
