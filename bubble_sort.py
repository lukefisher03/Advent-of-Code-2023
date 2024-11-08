# Implement Bubble Sort

array = [9, 2, 3, 5, 2, 3, 6, 2, 3, 6, 4, 58, 56]


def sort_array(arr) -> None:
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                tmp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp


sort_array(array)
print(array)
