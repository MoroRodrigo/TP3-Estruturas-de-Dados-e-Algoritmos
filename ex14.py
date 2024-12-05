def soma_lista(lista):
    # Caso base: Se a lista estiver vazia, soma é igual a 0
    if not lista:
        return 0
    # Caso recursivo: soma o primeiro elemento com a soma do restante da lista
    else:
        return lista[0] + soma_lista(lista[1:])

#Uso
resultado = soma_lista([1, 2, 3, 4])
print(resultado) 
