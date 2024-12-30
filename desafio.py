from typing import List

# 1. Media de valores de uma lista

def calcular_media(valores: List[float]) -> float:
    return sum(valores / len(valores))


# 2. Filtrar dados acima de uma limite

def filtrar_acima_de(valores: List[float], limite: float) -> list[float]:
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado

# a = filtrar_acima_de([0,15,10,5,4,8], 8)
# print(a)

# 3. Contar valores unicos em uma lista

def contar_valore_unicos(lista: List[int]) -> int:
    return len(set(lista))

# 4. Converter Celsius para Fahrenheit em uma Lista

def celsius_para_fahrenheit(temperaturas_celsius: List[float]) -> List[float]:
    return [(9/5) * temp + 32 for temp in temperaturas_celsius]

# 5. Calcular Desvio Padrão de uma Lista

def calcular_desvio_padrao(valores: List[float]) -> float:
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return variancia ** 0.5

# 6. Encontrar Valores Ausentes em uma Sequência

def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))

# a = encontrar_valores_ausentes([0,15,10,5,4,8])
# print(a)