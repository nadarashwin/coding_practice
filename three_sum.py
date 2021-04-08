# Given an array and a value, find if there is a triplet in array whose sum is equal to the given value. If there is such a triplet present in array, then print the triplet and return true. Else return false. 
# Example: 

# Input: array = {12, 3, 4, 1, 6, 9}, sum = 24;
# Output: 12, 3, 9
# Explanation: There is a triplet (12, 3 and 9) present
# in the array whose sum is 24. 

# Input: array = {1, 2, 3, 4, 5}, sum = 9
# Output: 5, 3, 1
# Explanation: There is a triplet (5, 3 and 1) present 
# in the array whose sum is 9. 


def three_sum(data, total):
    for i in range(len(data)-1):
        current = total - data[i]
        s = set()
        for j in range(i+1, len(data)):
            if (current - data[j]) not in s:
                s.add(data[j])
            else:
                return (data[i], data[j], current - data[j])

    return


#a = [1, 4, 45, 6, 10, 8]
a = [3, 7, 1, 2, 8, 4, 5]
#total = 22
total = 20
print(three_sum(a, total))