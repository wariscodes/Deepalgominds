arr = [10, 5, 20, 8, 15]

max_index = 0

for i in range(len(arr)):
    if arr[i] > arr[max_index]:
        max_index = i

print(max_index)