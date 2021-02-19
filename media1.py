"""
Programa: media.py
Descrição:
Este programa calcula a média de um número determinado de valores digitados
pelo usuário.
Data: 27/01/2021
Versão: 0.0.1
"""
# Entrada de dados
soma = 0

i = 0

numero_valores = int(input("Digite o número de valores que cuja média você deseja calcular: "))

while i < numero_valores:
    valor = float(input("Digite um valor: "))
    soma = soma + valor
    i += 1

# Processamento

media = soma/numero_valores

# Saída

print(f'A média dos valores digitados é {media}.')
