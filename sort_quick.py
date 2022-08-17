# def quick_sort(data, low, high):
#     i = low - 1
#     pivot = data[high]
#     for j in range(low, high):
#         if data[j] <= pivot:
#             print(f'data is {data[j]} and pivot is {pivot} and j is {j}')
#             i += 1
#             data[i], data[j] = data[j], data[i]
#             print(f'data-i is {data[i]} and data-j is {data[j]}')
#             print(data)
#     data[i+1], data[high] = data[high], data[i+1]
#     print(f'final data is {data}')
#     return(i+1)

# def quicker(data, low, high):
#     if low < high:
#         middle = quick_sort(data, low, high)
#         print(f'low is {low} and high is {high}')
#         quicker(data, low, middle -1)
#         quicker(data, middle+1, high)
#         print(f'pakka waala final {data}')

# data = [1,3,9,8,2,7,5]
# quicker(data, 0, len(data)-1)


def sorts(data, low, high):
    pivot = data[high]
    i = low - 1

    for j in range(low, high):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
            print(i,j,data[i],data[j])
    data[i+1], data[high] = data[high], data[i+1]
    return (i+1)


def quick_sort(data, low, high):
    if low < high:
        middle = sorts(data, low, high)
        quick_sort(data, low, middle-1)
        quick_sort(data, middle+1, high)


# data = [1,3,9,8,2,7,5]
data = [1,2,3,4,5]
data = [23,19,15,2,12,9]
quick_sort(data,0, len(data)-1)
print(data)
