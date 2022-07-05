# searching an element in an array
def binary_search(arr, start, end, key):
    mid = (start + end) // 2
    if key == arr[mid]:
        return mid
    elif mid == end:
        return 'Not Found'

    if key > arr[mid]:
        return binary_search(arr, mid+1, end, key)

    if key < arr[mid]:
        return binary_search(arr, start, mid-1, key)

arr = [5, 6, 7, 8, 9, 10]
binary_search(arr, 0, len(arr)-1, 10)

# inserting element into an array
def add_element(arr, n, key):
    arr.append(0)
    i = n - 1
    while i >= 0 and key < arr[i]:
        arr[i+1] = arr[i]
        i -= 1
    arr[i+1] = key
    print(arr)
arr = [10, 20, 30, 40, 50]
add_element(arr, len(arr), 12)

# deleting element from an array
def delete_element(arr, key):
    pos = binary_search(arr, 0, len(arr)-1, key)
    for i in range(pos, len(arr)-1):
        arr[i] = arr[i+1]
    print(arr)
arr = [10, 20, 30, 40, 50]
delete_element(arr, 10)
binary_search(arr, 0, 3, 50)