def inverter_string(string):
    # Caso base: Se a string estiver vazia, retorna a string vazia
    if not string:
        return ""
    # Caso recursivo: concatena o último caractere com a chamada recursiva sobre a string sem o último caractere
    else:
        return string[-1] + inverter_string(string[:-1])

#Uso:
resultado = inverter_string("recursao")
print(resultado)
