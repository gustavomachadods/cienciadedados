import math
'''
# Exercício 1
# Funções
def soma(a,b):
    soma = a + b
    return soma
# Entrada de dados
a = int(input("Informe o primeiro número: "))
b = int(input("Informe o segundo número: "))
# Processamento de dados
z = soma(a,b)
# Saída de dados
print('A soma dos números é igual a: ', z)
''''''
# Exercício 2
# Funções
def bruto(a):
    bruto = float(a*40)
    return bruto
def liquido(a):
    liquido = float(a*40*0.7)
    return liquido
def desconto(a):
    desconto = float(a*40*0.3)
    return desconto
# Entrada de dados
a = int(input("Informe o número de horas trabalhadas: "))
# Processamento de dados
x = bruto(a)
y = liquido(a)
z = desconto(a)
# Saída de dados
print('O valor do salário bruto é: R$', x)
print('O valor do salário líquido é: R$', y)
print('O valor dos descontos é: R$', z)
''''''
# Exercício 3
# Funções
def an(a1,n,r):
    an = a1+(n-1)*r
    return an
# Entrada de dados
a1 = int(input("Insira o 1º termo da P.A.: "))
n = int(input("Insira a posição do termo a descobrir: "))
r = int(input("Insira a razão: "))
# Processamento de dados
an = an(a1,n,r)
# Saída de dados
print('O termo é:', an)
''''''
# Exercício 4
# Funções
def an(a1,n,q):
    an = a1*q**(n-1)
    return an
# Entrada de dados
a1 = int(input("Insira o 1º termo da P.G.: "))
n = int(input("Insira a posição do termo a descobrir: "))
q = int(input("Insira a razão: "))
# Processamento de dados
an = an(a1,n,q)
# Saída de dados
print('O termo é:', an)
''''''
# Exercício 5
# Funções
def x(a,b):
    x = float(b/a)
    return x
# Entrada de dados
a = float(input("Insira o valor do primeiro termo: "))
b = float(input("Insira o resultado da equação: "))
# Processamento de dados
x = x(a,b)
# Saída de dados
print('O valor de x é:', x)
''''''
# Exercício 7
# Funções
def fv(pv,n,i):
    fv = pv*((1+(i/100))**n)
    return fv
# Entrada de dados
pv = int(input("Insira o Valor Presente: "))
n = float(input("insira o prazo de aplicação: "))
i = float(input("Insira a taxa de juros: "))
# Processamento de dados
fv = fv(pv,n,i)
# Saída de dados
print('O Valor Futuro será: R$', fv)
''''''
# Exercício 8
# Funções
def med(a,b,c,d):
    med = (a+b+c+d)/4
    return med
# Entrada de dados
a = float(input("Insira o primeiro número: "))
b = float(input("Insira o segundo número: "))
c = float(input("Insira o terceiro número: "))
d = float(input("Insira o quarto número: "))
# Processamento de dados
med = med(a,b,c,d)
# Saída de dados
print('A média dos números é: ', med)
''''''
# Exercício 10
# Funções
def d(r,p):
    d = r/p
    return d
# Entrada de dados
r = int(input("Renda do consumidor: "))
p = float(input("Preço do bem: "))
# Processamento de dados
q = d(r,p)
# Saída de dados
print('A quantidade demandada será de ', q)
''''''
# Exercício 11
# Funções
def dist(x1,y1,x2,y2):
    dist = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    return dist
# Entrada de dados
x1 = int(input("Coordenada x do ponto 1: "))
y1 = int(input("Coordenada y do ponto 1: "))
x2 = int(input("Coordenadas x do ponto 2: "))
y2 = int(input("Coordenadas y do ponto 2: "))
# Processamento de dados
dist = dist(x1,y1,x2,y2)
# Saída de dados
print('A distância entre os dois pontos é ', dist)
''''''
# Exercício 12
# Funções
def ordem(x1,x2,x3):
    ordem = sorted([x1,x2,x3])
    return ordem
# Entrada de dados
x1 = int(input("Número 1: "))
x2 = int(input("Número 2: "))
x3 = int(input("Número 3: "))
# Processamento de dados
ordem = ordem(x1,x2,x3)
# Saída de dados
print(ordem)
''''''
# Exercício 13
# Funções
def capm(rf,rm,b):
    capm = rf+b*(rm-rf)
    return capm
# Entrada de dados
rf = float(input("Retorno Livre de Risco: "))
rm = float(input("Retorno de Mercado: "))
b = float(input("Beta do Ativo: "))
# Processamento de dados
retorno = capm(rf,rm,b)
# Saída de dados
print(f'O Retorno Esperado do Ativo é {retorno}%.')
''''''
# Exercício 14
x = int(input("Número: "))
if x < 10:
    z = x*2
    print({z})
elif 10 < x < 20:
    z = x/2
    print({z})
else:
    print("Este número não é válido.")
''''''
# Exercício 15
x = int(input("Número: "))
if x < 0:
    print("Este número não é válido.")
elif x % 2 == 0:
    print("O número é par.")
elif x % 2 != 0:
    print("O número é ímpar.")
''''''
# Exercício 21
def imc(kg,m):
    imc = float(kg/(m**2))
    return imc
kg = float(input("Peso: "))
m = float(input("Altura: "))
imc = imc(kg,m)
if imc <= 18.5:
    print("Excessivamente magro")
elif 18.5 < imc <= 25:
    print("Peso normal")
elif 25 < imc <= 30:
    print("Sobrepeso")
else:
    print("Obeso")
'''
# Exercício 22
def wage(h):
    wage = h*20
    return wage
h = int(input("Carga horária: "))
wage = wage(h)
if wage <= 1000:
        print(f"Salário líquido: R$ {wage}")
elif 1000 < wage <= 2500:
    liq = wage*0.9
    print(f"Salário líquido: R$ {liq}")
elif 2500 < wage <= 5000:
    liq = wage*0.8
    print(f"Salário líquido: R$ {liq}")
else:
    liq = wage*0.65
    print(f"Salário líquido: R$ {liq}")


















