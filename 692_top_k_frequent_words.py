# Given an array of strings words and an integer k, return the k most frequent strings.
#
# Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
#
#
# Example 1:
#
# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:
#
# Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
# Output: ["the","is","sunny","day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.


def topKFrequent(words, k):
    """
    from collections import Counter
    words = sorted(Counter(words).items())
    return [x[0] for x in (sorted(words,key=lambda x: x[-1], reverse=True)[:k])]
    """

    from collections import Counter
    words = Counter(words)
    words = sorted(words, key=lambda x: (-words[x], x))
    return words[:k]

    """
    In [5]: w
    Out[5]: Counter({'i': 2, 'love': 2, 'leetcode': 1, 'coding': 1})

    In [11]: for i in w:
    ...:     print(i)
        ...:
    i
    love
    leetcode
    coding

    In [10]: for i in w:
        ...:     print(-w[i], i)
        ...:
        ...:
    -2 i
    -2 love
    -1 leetcode
    -1 coding
    """


words = ["i","love","leetcode","i","love","coding"]
k = 2
words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4

print(topKFrequent(words, k))
