def contar_repeticoes(string, caractere):
    # Caso base: Se a string estiver vazia, não tem mais ocorrências
    if not string:
        return 0
    # Caso recursivo: Se o primeiro caractere da string for igual ao alvo, soma 1
    elif string[0] == caractere:
        return 1 + contar_repeticoes(string[1:], caractere)
    # Caso recursivo: Se o primeiro caractere não for igual ao alvo, apenas chama a função para o restante da string
    else:
        return contar_repeticoes(string[1:], caractere)

#Uso
resultado = contar_repeticoes("banana", "a")
print(resultado)
