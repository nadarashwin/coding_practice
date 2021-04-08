listed_array = [13,12,11,5,6]

print(listed_array)

for i in range(len(listed_array)):
    print(i, listed_array[i])

print("**\n")

for i in range(len(listed_array) - 1):
    print(listed_array[i], listed_array[i+1])

for _ in range(1, len(listed_array)-1):
    for i in range(len(listed_array) - 1):
        if listed_array[i] > listed_array[i+1]:
            listed_array[i+1], listed_array[i] = listed_array[i], listed_array[i+1]
            print("Inside listed array is :", listed_array)
        print("Outside listed array is :", listed_array)

print("------")
print("final listed array is :", listed_array)

## 13,12,11,5,6

a = [13,12,11,5,6]
for _ in range(1, (len(a)-1)):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i+1], a[i] = a[i], a[i+1]
            print(a)

print(a)
[5, 6, 11, 12, 13]


a = [13,12,11,5,6]
for i in range(len(a)):
    swapped = False
    for j in range(0, len(a) - i - 1):
        if a[j] > a[j+1]:
            a[j+1], a[j] = a[j], a[j+1]
            swapped = True
    if not swapped:
        break
print("optimized solution for a is :", a)
[5, 6, 11, 12, 13]