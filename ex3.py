def torre_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        # Caso base: mover apenas um disco
        print(f"Mova o disco 1 do pino {origem} para o pino {destino}")
        return

    # Move os n-1 discos da origem para o auxiliar
    torre_hanoi(n-1, origem, auxiliar, destino)
    
    # Move o disco maior (n) da origem para o destino
    print(f"Mova o disco {n} do pino {origem} para o pino {destino}")
    
    # Move os n-1 discos do auxiliar para o destino
    torre_hanoi(n-1, auxiliar, destino, origem)

# Teste
numero_discos = 3
torre_hanoi(numero_discos, 'A', 'C', 'B')
