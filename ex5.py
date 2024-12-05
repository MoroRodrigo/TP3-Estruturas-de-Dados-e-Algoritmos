def quicksort(lista):
    # Caso base: listas com 0 ou 1 elemento já estão ordenadas
    if len(lista) <= 1:
        return lista

    # Escolha do pivô (aqui usamos o último elemento)
    pivo = lista[-1]

    # Divisão em sublistas
    menores = [x for x in lista[:-1] if x <= pivo]  # Elementos menores ou iguais ao pivô
    maiores = [x for x in lista[:-1] if x > pivo]   # Elementos maiores que o pivô

    # Ordenação das sublistas
    return quicksort(menores) + [pivo] + quicksort(maiores)

# Testando
numeros = [10, 7, 8, 1, 3, 9, 4, 5]
ordenados = quicksort(numeros)
print("Lista original:", numeros)
print("Lista ordenada:", ordenados)
