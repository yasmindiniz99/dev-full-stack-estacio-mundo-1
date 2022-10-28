idade = eval(input('Informe a idade da criança: '))
if idade < 5:
    print('A criança deve ser vacinada contra a gripe.')
    print('Procure o posto de saúde mais próximo.')
elif idade == 5:
    print('A vacina estará disponível em breve.')
    print('Aguarde as próximas informações.')
else:
    print('A vacinação só ocorrerá daqui a 3 meses.')
    print('Informe-se novamente nesse prazo.')
print('Cuide da saúde sempre. Até a próxima.')

#testes com o for
for item in range(5, 26, 5):
    print(item)

name = input('digite seu nome: \n')
for nome in name:
    print(nome)

nomes = ['Yasmin', 'Leticia', 'Sanji', 'Zoro']
for nome in nomes:
    print(nome)

#testes com while
palavra = input('Entre com uma palavra: \n')
while palavra != 'sair':
    palavra = input('Digite sair para sair do programa: ')
print('Fim da execução')

#while + uso de break

while True:
    print('Você está no primeiro laço')
    opcao1 = input('Deseja sair dele? Digite SIM para isso. \n')
    if opcao1 == 'SIM':
        break  #Break do primeiro laço
    else:
        while True:
            print('Você está no segundo laço. \n')
            opcao2 = input('Deseja sair dele? Digite SIM para isso. \n')
            if opcao2 == "SIM":
                break  #break do segundo laço
        print('Você saiu do segundo laço')
print('Você saiu do primeiro laço.')

#usando a instrução continue, imprima todos os números inteiros de 1 a 10, pulando apenas o 5:
for num in range(1, 11):
    if num == 5:
        continue
    else:
        print(num)
print('Laço encerrado')

#Mesma coisa que o de cima, porém com um input (NÃO FUNCIONA)
# for num in range(eval(input('Digite dois numeros: (x, y)8'))):
#     if num == 5:
#         continue
#     else:
#         print(num)
# print('Laço encerrado')

#imprimir apenas numeros impares
for num in range (1, 11):
    if num % 2 == 0:
        pass
    else:
        print(num)
print("laço encerrado.")

#ou
for num in range(1, 11):
    if num % 2 == 1:
        print(num)
print('Laço encerrado')

#Exercicios 1 e 2 - mod 1
s = 0
for i in range(5):
    s += 3*i
print(s)

s = 0
a = 1
while s < 5:
    s = 3*a
    a += 1
    print(s)

#Exemplo 1: Implementar uma solução em Python que retorne o menor elemento de uma lista.
def encontrar_minimo(lista):
    minimo = lista[0]
    for elem in lista:
        if(elem < minimo):
            minimo = elem
    return minimo
lista_teste = [5, 3, 6, 3, 7, 0, 3, 1]
menor = encontrar_minimo(lista_teste)
print('O menor elemento da lista é: [{}]'.format(menor))

#Exercício 1:Implementar uma solução em Python que retorne a soma de todos os elementos pares de uma lista
def soma_pares(soma):
    elem = 0
    for i in soma:
        if i % 2 == 0:
            elem += i
        else:
            elem = elem
    return elem

lista_teste_2 = [0,1,2,3,4,5,6]
soma = soma_pares(lista_teste_2)
print('A soma de todos os elementos pares da lista de teste 2 é: [{}]'.format(soma))

#Ou
def ehPar(n):
    r = (n%2==0)
    return r

def soma_par(lst):
    soma = 0
    for num in lst:
        if(ehPar(num)):
            soma = soma + num
    return soma

lista = [10, 2, 5, 7, 6, 3]
soma = soma_par(lista)
print(f'O somatório dos elementos pares da lista é: [{soma}]')

#Exercício 2: Implementar uma solução em Python que caulcule o fatorial de um número.
#OBS: O fatoria n! = n.(n-1) | fatorial de 0! =1 | Fatorial de 1! = 1
#estrategia_1
def fatorial_iterativo(n):
    f=1
    for i in range(1,n+1):
        f=f*i
        return f
#estrategia_2
def fatorial_recursivo(n):
    if((n==0)or(n==1)):
        return 1
    return n*fatorial_recursivo(n-1)

numero = 5
print(f'O fatorial de {numero} é: {fatorial_recursivo(numero)}')
print(f'O fatorial de {numero} é: {fatorial_iterativo(numero)}')

#Exercício 3: Implementar uma solução em Python que determine se um número é ou não primo.
#OBS: Um número só é primo se ele SÓ for divisivel por ele mesmo e por um

def ehPrimo(n):
    if(n<2):
        return False
    i=n//2
    while(i>1):
        if(n%1==0):
            return False
        i=i-1
    return True

def imprimir_resultado(numero, resultado):
    mensagem = f'O número {numero} NÃO é primo'
    if(resultado):
        mensagem = f'O número {numero} é primo'
    return mensagem

numero = 4
resultado = ehPrimo(numero)
msg=imprimir_resultado(numero, resultado)
print(msg)

#função dentro do if-else que pede que você dê um numero entre um e dois e retorna a soma dele com 10
escolha = input('Escolha um número entre 1 e 2 e execute uma função: ')
if escolha == '1':
    def func1(x):
        return x + 1
    s = func1(10)
else:
    def func2(x):
        return x + 2
    s = func2(10)

print(s)

#Mostra a utilização da chamada de um parâmetro real quando se há um parâmetro padrão associado.
def taximetro(distancia, multiplicador=1):
    largada = 3
    km_rodado = 2
    valor = (largada + distancia + km_rodado) * multiplicador
    return valor

pagamento = taximetro(3.5)
print(pagamento)

#Função com corpotamento de procedimento:
def func1(x):
    x = 10
    print(f'função func1 - x = {x}')

def func2(x):
    x = 20
    print(f'func2 - x = {x}')

x = 0
func1(x)
func2(x)
print(f'Programa principal - x = {x}')

#Mesmo código acima, mas que altera a variavel global x.
def func3():
    global x
    x = 30
    print(f'Função func1 - x = {x}')

def func4():
    global x
    x = 40
    print(f'Função func2 - x = {x}')

x = 0
func3()
func4()
print(f'Programa principal - x = {x}')

#Calcula o valor a pagar para o taxista com base na distância percorrida
def taximetro2(distancia):
    def calculaMult():
        if distancia < 5:
            return 1.2
        else:
            return 1
    multiplicador = calculaMult()
    largada = 3
    km_rodado = 2
    valor = (largada + distancia + km_rodado) * multiplicador
    return valor

dist = eval(input('Entre com a distância a ser percorrida em km: '))
pagamento = taximetro(dist)
print(f'O valor a pagar é de R$ {pagamento}')

#Utilizando uma função recursiva:
def regressiva(x):
    print(x)
    regressiva(x - 1)

#define a condição de parada para que o sistema não venha a sofrer algum erro por falta de memória
def regressiva2(x):
    if x <= 0:
        print('Acabou')
    else:
        print(x)
        regressiva2(x-1)

#calculando um numero fatorial com uma implementação recursiva
def fatorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n*fatorial(n-1)

#Função fatorial de forma não recursiva:
def fatorial2(n):
    fat = 1
    if n == 0 or n == 1:
        return fat
    else:
        for x in range(2, n+1):
            fat = fat*x
        return fat

#Possível implementação recursiva de função que determina o n-ésimo termo da sequência de Fibonacci:
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)  #traz a chamada recursiva para calcular os dois termos anteriores da sequência.

#declarando um docstring para a função:

#Função que determina o n-ésimo termo da sequência de fibonacci
def fibo2(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo2(n-1) + fibo2(n-2)

print(help(fibo2))

# Bibliotecas: ver os segundos documentos dessa mesma missão

#Tratamento de exceções em outro documento tbm
