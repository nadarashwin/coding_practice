a = [13,12,11,5,6]

print(a)

def merge_sort(data):
    if len(data) > 1:
        mid_way = len(data) // 2

        left = data[:mid_way]
        right = data[mid_way:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1


data = [13,12,11,5,6]

merge_sort(data)
print(data)
