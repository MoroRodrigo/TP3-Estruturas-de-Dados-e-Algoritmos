def fibonacci(n, memo={}):
    # Verifica se o valor já foi calculado
    if n in memo:
        return memo[n]
    
    # Caso base
    if n <= 1:
        return n
    
    # Calcula e armazena o valor de Fibonacci
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# Teste
print(fibonacci(10))  # Saída: 55
