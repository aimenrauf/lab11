import time
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

array = list(range(1000000))
key = 999999  
start = time.time()
result = linear_search(array, key)
end = time.time()
print(f"Element found at index: {result}")
print(f"Time taken: {end - start:.6f} seconds")