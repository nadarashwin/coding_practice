a = [13,12,11,5,6]

print(a)
for i in range(1, len(a)):
    key = a[i]

    # Move elements of a[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    j = i-1
    while j >= 0 and key < a[j]:
        a[j + 1] = a[j]
        j -= 1
        print(a, "inside while")
    a[j + 1] = key
    print(a, "inside for")

print(a)
