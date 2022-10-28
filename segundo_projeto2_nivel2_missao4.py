# Exemplo 1
# Implementar uma solução em Python que calcule as raízes de uma esquação do segundo grau:
# Dada a equação x**2 + 5x + 6 == 0, as raízes são {-3, -2}
# Equação de 2o grau: f(x) = ax**2 + bx + c
# Encontrar o valor de x que vai zerar a função
# delta = b**2 - 4 * a * c e depois as raízes: x = -b +- raiz de delta /2*a
# Se o delta for negativo, a equação não possui raizes nos reais
# Se o delta for igual a 0, só havera uma raiz


import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk


def entrada_dados():
    coeficiente = eval(input('Digite o valor do coeficiente: '))
    return coeficiente


def calc_delta(a, b, c):
    delta = (b*b) - (4 * a * c)
    return delta


def calcular_raizes(a, b, c, delta):
    if delta < 0:
        resultado = 'A equação não possui raizes nos números reais.'
    elif delta == 0:
        x = -b / (2 * a)
        resultado = f'A equação possui apenas a raíz {x}'
    else:
        x1 = (-b - np.sqrt(delta)) / (2 * a)
        x2 = (-b + np.sqrt(delta)) / (2 * a)
        resultado = f'A equação possui as raízes: ({x1}, {x2})'
    return resultado


# f(x) = ax^2 + bx + c
a = entrada_dados()
b = entrada_dados()
c = entrada_dados()
delta = calc_delta(a, b, c)
resultado = calcular_raizes(a, b, c, delta)
print(resultado)


#criar um gráfico de barras (usei o estilo cyberpunk)
x = np.array(['A', 'B', 'C', 'D'])
y = np.array([3, 8, 1, 10])
plt.style.use('cyberpunk')
plt.bar(x, y)

plt.ylabel("y")
plt.xlabel("x")
plt.title("Um gráfico para teste")
plt.show()

#Implemetar uma solução em Python para gerar 1000 pontos seguindo a distribuição Normal, com média 20 e desvio-padrão 2. Além disso exiba os dados em um histógrama.
np.random.seed(1)
dados = np.random.normal(loc=20, scale=2, size=1000)
plt.hist(dados, ec='pink')
plt.show()

#smtplib na folha de enviar email

#modulo time
import time

x = time.time()
print(f'Local time: {time.ctime(x)}')

#Criar a primeira janela com alguns elementos no tkinter em outra folha

