# merge sort
import math
def mergesort(arr):
    if len(arr) > 1:
        # mid = len(arr)//2
        mid = math.ceil(len(arr)/2)
        l = arr[:mid]
        r = arr[mid:]
        # print(l, r, arr)
        mergesort(l)
        mergesort(r)
        i = j = k = 0
        while i < len(l) and j < len(r):
            # print('begins')
            # print(i, j, k, arr)
            # print('l : ', l, 'r : ', r)
            if l[i] < r[j]:
                arr[k] = l[i]
                print('l_arr : ', arr)
                i += 1
            else:
                arr[k] = r[j]
                print('r_arr : ', arr)
                j += 1
            k += 1
        while i < len(l):
            # print('l : ', l, 'r : ', r)
            # print('l_pre : ', arr)
            arr[k] = l[i]
            i += 1
            k += 1
            # print('l_post : ', arr)

        while j < len(r):
            # print('l : ', l, 'r : ', r)
            # print('r_pre : ', arr)
            arr[k] = r[j]
            j += 1
            k += 1
            # print('r_post : ', arr)


arr = [4, 0, 6, 1, 5, 2, 3]
mergesort(arr)