def linear_search(arr, key):
    count = 0
    for i in range(len(arr)):
        count +=1
        if arr[i] == key:
            print("Element found on index: ",i," Iterations = ",count)
            return
    return -1

def binary_search(arr, key):
    count =0
    left = 0
    right = len(arr) - 1
    while left <= right:
        count +=1
        mid = (left + right) // 2
        if arr[mid] == key:
            print("Element found on index: ",mid," Iterations = ",count)
            return
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return print("Data not found")

array1 = [169,23,56,12,134,78,34,90,103,67,89,45]
array2 = [12,23,34,45,56,67,78,89,90,103,134,169]
key = 45
print("Linear for unsorted data:")
linear_search(array1,key)
print("Binary for unsorted data:")
binary_search(array1,key)

print("Linear for Sorted")
linear_search(array2,key)
print("Binary for Sorted")
binary_search(array2,key)