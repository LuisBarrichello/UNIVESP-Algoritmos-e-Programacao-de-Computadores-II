def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Se o elemento do meio é o alvo, retorna o índice
        if arr[mid] == target:
            return mid
        
        # Se o alvo está na metade esquerda, atualiza o limite direito
        elif arr[mid] > target:
            right = mid - 1
        
        # Se o alvo está na metade direita, atualiza o limite esquerdo
        else:
            left = mid + 1
    
    # Se o elemento não está presente na lista, retorna -1
    return -1

# Exemplo de uso:
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11
result = binary_search(arr, target)
if result != -1:
    print(f"Elemento {target} encontrado no índice {result}.")
else:
    print(f"Elemento {target} não encontrado na lista.")
