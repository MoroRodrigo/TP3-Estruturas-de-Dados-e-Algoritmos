def quickselect(lista, k):
    # A função de particionamento
    def partition(lista, low, high):
        pivo = lista[high]
        i = low - 1
        for j in range(low, high):
            if lista[j] <= pivo:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
        lista[i + 1], lista[high] = lista[high], lista[i + 1]
        return i + 1
    
    low, high = 0, len(lista) - 1
    
    while low <= high:
        # Particiona a lista
        pi = partition(lista, low, high)
        
        # Verifica se o pivô está na posição k
        if pi == k:
            return lista[pi]
        elif pi < k:
            # Busca à direita do pivô
            low = pi + 1
        else:
            # Busca à esquerda do pivô
            high = pi - 1

# Testando o algoritmo
numeros = [10, 7, 8, 1, 3, 9, 4, 5]
k = 3  # Procurando o tericeiro menor elemento
resultado = quickselect(numeros, k - 1) 
print(f"O {k}-ésimo menor elemento é:", resultado)
