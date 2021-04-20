# Given a dictionary sort the dict by value and for similar values, sort it by key

def sort_dict(data):
    # OrderedDict preserves the order in which the keys are inserte
    # from collections import OrderedDict
    # data = OrderedDict(sorted(data.items()))

    # return sorted(data.items(), key=lambda x: x[-1], reverse=True)

    data = sorted(data.items()) # returns list of tuples
    return sorted(data, key=lambda x: x[-1], reverse=True)



data = {'abc':30, 'bcd': 10, 'jkl':40, 'cde': 40, 'def': 35, 'efg': 10, 'fgh': 50, 'ghi': 40, 'hij':23}

print(sort_dict(data))