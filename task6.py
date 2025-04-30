def binary_search_iterative(arr, key):
    count = 0
    left = 0
    right = len(arr) - 1
    while left <= right:
        count+=1
        mid = (left + right) // 2
        if arr[mid] == key:
            print("element found on index: ",mid," Iteration = ",count)
            return
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search_recursive(arr, left, right, key,count):
    
    if left > right:
        return -1
    mid = (left + right) // 2
    count +=1
    if arr[mid] == key:
        print("element found on index: ",mid," Iteration = ",count)
        return
    elif arr[mid] < key:
        return binary_search_recursive(arr, mid + 1, right, key,count)
    else:
        return binary_search_recursive(arr, left, mid - 1, key,count)

array = [2,4,5,7,12,16,23,34,45,56]
key = 34
print("for iterative")
binary_search_iterative(array,key)
print("for recursive function")
binary_search_recursive(array,0,len(array)-1,key,0)