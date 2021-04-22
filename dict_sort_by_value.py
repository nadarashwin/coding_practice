# Given a dictionary sort the dict by value and for similar values, sort it by key

def sort_dict(data):
    ## First Way
    # OrderedDict preserves the order in which the keys are inserte
    # from collections import OrderedDict
    # data = OrderedDict(sorted(data.items()))

    # return sorted(data.items(), key=lambda x: x[-1], reverse=True)

    ## Second way
    # data = sorted(data.items()) # returns list of tuples
    # return sorted(data, key=lambda x: x[-1], reverse=True)

    ## Third way - Explaination at the botton
    data = sorted(data, key=lambda x: (-data[x], x))
    return data[:2]



data = {'abc':30, 'bcd': 10, 'jkl':40, 'cde': 40, 'def': 35, 'efg': 10, 'fgh': 50, 'ghi': 40, 'hij':23}

print(sort_dict(data))


## returns a list for the dictionary
In [119]: sorted(data)
Out[119]: ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'jkl']

## returns the key by sorting the value in ascending order
In [127]: sorted(data, key=lambda x: data[x])
Out[127]: ['bcd', 'efg', 'hij', 'abc', 'def', 'jkl', 'cde', 'ghi', 'fgh']

## returns the key by sorting the value in descending order and if the value is same sort by the key
## -data[x] means sorting is reverse with the negative sign
## and the x next to it means if -data[x] are equal, compare by alphabetical (keys in this case)
In [128]: sorted(data, key=lambda x: (-data[x], x))
Out[128]: ['fgh', 'cde', 'ghi', 'jkl', 'def', 'abc', 'hij', 'bcd', 'efg']


## returns a list of tuples for the dictionary
In [120]: sorted(data.items())
Out[120]:
[('abc', 30),
 ('bcd', 10),
 ('cde', 40),
 ('def', 35),
 ('efg', 10),
 ('fgh', 50),
 ('ghi', 40),
 ('hij', 23),
 ('jkl', 40)]