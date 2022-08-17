a = [13,12,11,5,6]

print(a)

a = [13,12,11,5,6]
for i in range(len(a)):
    start_index = i
    for j in range(i + 1, len(a)):
        if a[start_index] > a[j]:
            start_index = j
    a[i], a[start_index] = a[start_index], a[i]

print(a)
[5, 6, 11, 12, 13]