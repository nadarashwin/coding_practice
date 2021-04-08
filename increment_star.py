def recursion(number):
    print('*' * number)
    if number == 4:
        return 4
    return(recursion(number + 1) * number)

print(recursion(1))