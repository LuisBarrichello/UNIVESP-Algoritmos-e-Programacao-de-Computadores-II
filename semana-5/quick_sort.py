def quick_sort(v, ini, fim):
    meio = (ini + fim) // 2
    pivo = v[meio]
    i = ini
    j = fim
    while i <= j:
        while v[i] < pivo:
            i += 1
        while v[j] > pivo:
            j -= 1
        if i <= j:
            v[i], v[j] = v[j], v[i]
            i += 1
            j -= 1
    if j > ini:
        quick_sort(v, ini, j)
    if i < fim:
        quick_sort(v, i, fim)

arr = [64, 34, 25, 12, 22, 11, 90]
quick_sort(arr, 0, len(arr) - 1)
print("Array ordenado:")
for i in range(len(arr)):
    print(arr[i], end=" ")
