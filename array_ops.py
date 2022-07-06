# element appearing only once in an array
def find_nonrep(arr):
    val = arr[0]
    for i in range(1, len(arr)):
        val = val^arr[i]
    return val
arr = [7, 3, 5, 4, 5, 3, 4, 7, 8]
find_nonrep(arr)

# find the repetitive element for array with elements 1 to n
# using hashing
def find_dup(arr):
    s = set()
    for i in range(len(arr)):
        if arr[i] in s:
            return arr[i]
        s.add(arr[i])
arr = [1, 1, 2, 3]
arr = [9, 8, 2, 6, 1, 8, 5, 3, 4]
find_dup(arr)