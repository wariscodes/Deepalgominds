def merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)

    i = n - 1   # last of arr1
    j = 0       # first of arr2

    while i >= 0 and j < m:

        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
            i -= 1
            j += 1
        else:
            break

    print(arr1)
    print(arr2)


arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 6, 8, 9]

merge(arr1, arr2)