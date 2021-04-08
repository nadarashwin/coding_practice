def partition(arr, low, high):
	pivot = arr[high]
	i = (low - 1)

	for j in range(low, high):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
			print("inside loop", arr, j)
	arr[i+1], arr[high] = arr[high], arr[i+1]
	print(i, j)
	return(i + 1)

def quick_sort(arr, low, high):
	if low < high:

		pi = partition(arr, low, high)
		
		quick_sort(arr, low, pi-1)
		quick_sort(arr, pi+1, high)








data = [5,7,9,10,2]
data = [10, 7, 8, 9, 2, 1, 5] 
print(data)
quick_sort(data, 0, len(data)-1)
print(data)