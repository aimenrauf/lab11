def linear_search(arr,key):
    count = 0
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

array = ["Aimen","Haseeb","Sania","Rauf","Sadaf"]
key = "Haseeb"
print("String found on index: ",linear_search(array,key))