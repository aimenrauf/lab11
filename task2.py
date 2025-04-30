def linear_search(arr,key):
    count = 0
    for i in range(len(arr)):
        if arr[i] == key:
            print("Element 6 found on index: ",i)
            return
    print("element not found")
    return

array1 = [1,2,3,4,5,6,7,8,9,10]
array2 = [2]*1000
key = 6
print("for array1:")
linear_search(array1,key)
print("for array2")
linear_search(array2,key)