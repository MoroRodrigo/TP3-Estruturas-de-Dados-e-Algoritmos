import os

def listar_conteudo_diretorio(caminho, nivel=0):
    """
    Percorre um diretório e lista todos os arquivos e subdiretórios.
    """
    try:
        # Lista o conteúdo do diretório
        conteudo = os.listdir(caminho)
        
        # Itera sobre cada item no conteúdo do diretório
        for item in conteudo:
            caminho_completo = os.path.join(caminho, item)  # Caminho absoluto ou relativo do item
            indentacao = "  " * nivel  # Indenta para indicar o nível de profundidade
            
            if os.path.isdir(caminho_completo):
                # Se o item é um diretório, exibe o nome e entra nele recursivamente
                print(f"{indentacao}[D] {item}/")
                listar_conteudo_diretorio(caminho_completo, nivel + 1)
            else:
                # Se o item é um arquivo, apenas exibe o nome
                print(f"{indentacao}[A] {item}")
    except PermissionError:
        # Tratamento para diretórios que não temos permissão de acessar
        print(f"{'  ' * nivel}[X] Permissão negada: {caminho}")
    except FileNotFoundError:
        # Tratamento para caminhos inválidos ou diretórios inexistentes
        print(f"[!] Diretório não encontrado: {caminho}")
    except Exception as e:
        # Tratamento genérico de erros
        print(f"[!] Erro ao acessar '{caminho}': {e}")

# Caminho inicial para testar a função
caminho_inicial = input("Digite o caminho do diretório que deseja explorar: ")
listar_conteudo_diretorio(caminho_inicial)
