def interpolation_search(arr, key):
    count = 0
    low = 0
    high = len(arr) - 1
    while low <= high and arr[low] <= key <= arr[high]:
        count +=1
        pos = low + ((key - arr[low]) * (high - low) // (arr[high] - arr[low]))
        if arr[pos] == key:
            print("key found on index: ",pos," and number of iteration = ",count)
            return
        elif arr[pos] < key:
            low = pos + 1
        else:
            high = pos - 1
    return -1

array1 = [1,5,7,12,13,16,17,23,36,56,120,778]
array2 = [20,30,40,50,60,70,80,90,100,110,120]
key = 120
print("for UNordered array")
interpolation_search(array1,key)
print("for Ordered array")
interpolation_search(array2,key)