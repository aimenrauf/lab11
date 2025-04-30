def binary_search(arr, key):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1

array1 = [169,23,56,12,134,78,34,90,103,67,89,45]
key = 45
print("for unsorted data:")
print("Found at index: ",binary_search(array1,key))
array2 = [12,23,34,45,56,67,78,89,90,103,134,169]
print("if data is sorted:")
print("Found at index: ",binary_search(array2,key))