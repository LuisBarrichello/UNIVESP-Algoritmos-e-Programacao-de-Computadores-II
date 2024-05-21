def heapify(arr, n, i):
    largest = i  # Inicializa o maior como raiz
    left = 2 * i + 1  # Esquerda = 2*i + 1
    right = 2 * i + 2  # Direita = 2*i + 2

    # Verifica se o filho da esquerda da raiz existe e se é maior que a raiz
    if left < n and arr[i] < arr[left]:
        largest = left

    # Verifica se o filho da direita da raiz existe e se é maior que a raiz
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Troca a raiz se necessário
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        # Heapifica a subárvore afetada
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Constrói um heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrai elementos um por um
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

# Exemplo de uso:
arr = [64, 34, 25, 12, 22, 11, 90]
heap_sort(arr)
print("Array ordenado:")
for i in range(len(arr)):
    print(arr[i], end=" ")

    
