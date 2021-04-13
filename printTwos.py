# Write a function that takes in a number as argument and returns a string composed of an odd number multiplied by 2s such that the final value is equal to n. 
# There should be an equal number of 2s on both sides. Extra 2 should appear at the front of the string. Note: The value of the odd number can be 1. 


# >>> printTwos(2) '2 * 1'  
# >>> printTwos(10) '2 * 5'  
# >>> printTwos(20) '2 * 5 * 2'  
# >>> printTwos(30) '2 * 15'  
# >>> printTwos(32) '2 * 2 * 2 * 1 * 2 * 2' 
# >>> printTwos(80) '2 * 2 * 5 * 2 * 2' 

def printTwos(data):
    temp_array = []
    while data:
        if data % 2 == 0:
            temp_array.append(2)
            data = data // 2
        else:
            temp_array.append(data)
            break   ## halt the infinite loop
    
    mid = len(temp_array) // 2 ## get the mid of temp_array
    temp = temp_array.pop() ## capture the last element
    temp_array.insert(mid, temp) ##  insert the last element in the midle of the temp_array

    return ' * '.join(list(map(str, temp_array)))
    

print(printTwos(2))
print(printTwos(10))
print(printTwos(20))
print(printTwos(30))
print(printTwos(32))
print(printTwos(80))
