def binary_search(arr, key):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return False

array = [12,23,34,45,56,67,78,89,90,103,134,169]
key = 45
print("Found in array? ",binary_search(array,key))