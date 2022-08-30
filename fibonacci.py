def fibonacci(n):
    # ------FIRST WAY------
    # Time Complexity:Exponential,as every function calls two other functions.

    # if n <= 1:
    #     return n
    # return fibonacci(n-1) + fibonacci(n-2)

    # ------SECOND WAY------
    cache = {0: 0, 1: 1}

    if n in cache:
        return cache[n]
    cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]

    # ------THIRD WAY------
    # temp = [0, 1]

    # for i in range(2, n+1):
    #     temp.append(temp[i-1] + temp[i-2])

    # return temp[-1]


print(fibonacci(5))
print(fibonacci(6))
