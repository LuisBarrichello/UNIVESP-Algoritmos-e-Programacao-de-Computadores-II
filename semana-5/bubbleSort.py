import time

def bubble_sort(vetor):
    size = len(vetor)
    for i in range(size-1):
        for j in range(size-i-1):
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]


arr = [64, 34, 25, 12, 22, 11, 90]
start_time = time.time()
bubble_sort(arr)
end_time = time.time()
print("Array ordenado:")
for i in range(len(arr)):
    print(arr[i], end=" ")


print("\nTempo de execução:", end_time - start_time, "segundos")