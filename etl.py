import csv

def ler_csv(nome_arquivo: str) -> list[dict]:
    """
    Funcao para ler um arquivo csv e retorna uma lista
    de dicionarios
    """
    lista = []
    with open(nome_arquivo, mode="r", encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
    """
    Funcao para filtar produtos onde entregue = True
    """
    lista_produtos_filtrados = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_produtos_filtrados.append(produto)
    return lista_produtos_filtrados

def somar_valores_dos_produtos(lista_produtos_filtrados: list[dict]) -> list[dict]:
    """
    Funcao para somar os produtos
    """
    valor_total = 0
    for produto in lista_produtos_filtrados:
        valor_total += int(produto.get("price"))
    return valor_total


