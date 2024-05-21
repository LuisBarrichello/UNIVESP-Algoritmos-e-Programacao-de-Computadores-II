def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid] # slicing
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i +=1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def merge_sort_wrapper(arr):
    merge_sort(arr)


# Exemplo de uso:
arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort_wrapper(arr)
print("Array ordenado:")
for i in range(len(arr)):
    print(arr[i], end=" ")
