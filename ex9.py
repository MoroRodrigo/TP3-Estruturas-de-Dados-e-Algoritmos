class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


def percorre_em_ordem(no, resultado=None):
    if resultado is None:
        resultado = []
    
    # Verifica se o nó é nulo
    if no is not None:
        # Primeiro, percorre a subárvore esquerda
        percorre_em_ordem(no.esquerda, resultado)
        
        # Depois, adiciona o valor do nó atual
        resultado.append(no.valor)
        
        # Por fim, percorre a subárvore direita
        percorre_em_ordem(no.direita, resultado)
    
    return resultado

#Aplicando

# Cria a árvore binária
raiz = No(10)
raiz.esquerda = No(5)
raiz.direita = No(15)
raiz.esquerda.esquerda = No(3)
raiz.esquerda.direita = No(7)
raiz.direita.esquerda = No(12)
raiz.direita.direita = No(18)

# Percorre a árvore em ordem
resultado = percorre_em_ordem(raiz)
print("Valores em ordem:", resultado)
