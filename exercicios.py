print("Hello, World!")

# Soma
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
soma = x + y
print(f"A soma dos valores é {soma}.")

# Nome
nome = input("Qual seu nome? ")
print(f"Oi, {nome}.")

#Salário
hora = int(input("Quantas horas trabalhadas? "))
hora_aula = 40
bruto = hora * hora_aula
liquido = bruto * 0.7
desconto = bruto * 0.3
print(f"Salário bruto: R$ {bruto}")
print(f"Saláro líquido: R$ {liquido}")
print(f"Desconto: R$ {desconto}")

# PA

# PG

# Equação Linear
print("Equação: a.x = b")
a = float(input("a = "))
b = float(input("b = "))
x = b / a
print(f"O valor de x é {x}")

# Equação de segundo grau
import math
print("Equação: ax² + bx + c = 0")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
x1 = (-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
x2 = (-b-math.sqrt((b**2)-(4*a*c)))/(2*a)
print(f"O valor de x é {x1} ou {x2}.")

# Capitalização
valor = float(input("Valor inicial: "))
prazo = int(input("Prazo de investimento (em meses): "))
taxa = float(input("Taxa de juros (mensal): "))
taxa = taxa/100
taxa = 1+taxa
final = valor*(taxa**prazo)
print(f"Valor final: R$ {final}")

# Média
a = float(input("Número 1: "))
b = float(input("Número 2: "))
c = float(input("Número 3: "))
d = float(input("Número 4: "))
x = (a+b+c+d)/4
print(f"A média é {x}.")


# Área e perímetro de um círculo
import math
def area(r):
    area = math.pi*(r**2)
    return area
def perimetro(r):
    perimetro = 2*math.pi*r
    return perimetro
r = float(input("Insira o valor do raio: "))
a = area(r)
b = perimetro(r)
print(f"Área = {a}; Perímetro = {b}.")
