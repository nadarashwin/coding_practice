# Write a function that takes two lists that returns a dict with keys from the first list and values from the second list. eg.
# 1. makedict(['a', 'b', 'c'],[1,2,3]) gives {‘a’:1,’b’:2,’c’:3}
# 2. makedict(['a', 'b', 'c'],[1,2,3,4,5]) gives {‘a’:1,’b’:2,’c’:[3,4,5]}

def club_dict(list1, list2):
    temp_dict = {}
    # for index in range(len(list1)):
    #     if index == (len(list1) - 1):
    #         temp_dict[list1[index]] = list2[index:]
    #         break
    #     temp_dict[list1[index]] = list2[index]

    for index in range(len(list1) - 1):
        temp_dict[list1[index]] = list2[index]

    temp_dict[list1[len(list1) - 1]] = list2[(len(list1) - 1):]

    return temp_dict


a = ['a', 'b', 'c']
b = [1, 2, 3, 4, 5]
print(club_dict(a, b))
