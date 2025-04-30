def binary_search(arr, key):
    count = 0
    left = 0
    right = len(arr) - 1
    while left <= right:
        count +=1
        mid = (left + right) // 2
        if arr[mid] == key:
            print("Element found on index = ",mid," iterations = ",count)
            return
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def interpolation_search(arr, key):
    count =0
    low = 0
    high = len(arr) - 1
    while low <= high and arr[low] <= key <= arr[high]:
        count +=1
        pos = low + ((key - arr[low]) * (high - low) // (arr[high] - arr[low]))
        if arr[pos] == key:
            print("Element found on index = ",pos," iterations = ",count)
            return
        elif arr[pos] < key:
            low = pos + 1
        else:
            high = pos - 1
    return -1

array = list(range(1000))  
key = 999
print("for Binary Search:")
binary_search(array,key)
print("for interpolation search:")
interpolation_search(array,key)