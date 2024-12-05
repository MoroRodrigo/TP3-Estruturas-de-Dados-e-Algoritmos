def eh_palindromo(palavra):
    # Remove espaços e converter para minúsculas
    palavra = palavra.replace(" ", "").lower()
    
    # Caso base: Se a palavra tiver 0 ou 1 caractere, é um palíndromo
    if len(palavra) <= 1:
        return True
    
    # Verifica se o primeiro e o último caractere são iguais
    if palavra[0] == palavra[-1]:
        # Chamada recursiva removendo o primeiro e o último caractere
        return eh_palindromo(palavra[1:-1])
    else:
        return False

#Uso
print(eh_palindromo("radar"))  # True
print(eh_palindromo("hello"))  # False
print(eh_palindromo("A man a plan a canal Panama"))  # True
