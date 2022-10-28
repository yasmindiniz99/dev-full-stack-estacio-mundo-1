#Implementar uma solução em Python que faça o tratamento de exceção para verificar se a entrada é de fato um número
try:
    x = int(input('Digite um número: '))
except ValueError:
    print('Entre com um número válido.')


#Implementar uma solução em Python que faça o tratamento de exceção para verificar se uma entrada é numérica e que, além disso, insista que o usuário digite um número válido.
#Minha solução
def numeroValido():
    x = int(input('Digite um número: '))
    return x

def verifica():
    try:
        numeroValido()
    except ValueError:
        print('Entre com um número válido.')
        verifica()


verifica()


#Solução do professor
while True:
    try:
        x = int(input('Digite um numero:'))
        break
    except ValueError:
        print('Entre com um número válido.')


# Implementar uma solução em Python que faça o tratamento de exceção de divisão por zero.
# Minha solução
b = int(input('Digíte o valor de b: '))


while True:
    try:
        a = int(input('Digíte um valor maior que 0 para a: '))
        x = b / a
        print(f'O valor de x=b/a é igual a {x}, sendo que a é indicado pelo número {a} e b pelo número {b}')
        break
    except ZeroDivisionError:
        print('Por favor, digíte um valor maior que zero.')



# Solução do professor
def dividir(x, y):
    try:
        resultado = x / y
        print('A resposta é: ', resultado)
    except ZeroDivisionError:
        print('Divisão por zero.')


dividir(3, 0)
dividir(3, 2)

# Tratamento de exceção
try:
    num = eval(input('Entre com um número inteiro: '))
    print(num)
except:
    print('Entre com o valor númerico e não letras.')


# Tratamento de exceção com determinado tipo
try:
    num = eval(input('Entre com um número inteiro: '))
    print(num)
except NameError:
    print('Entre com o valor númerioc e não letras.')

# Tratamento de exceções de múltiplos tipos:
try:
    num = eval(input('Entre com um número inteiro: '))
    print(num)
except ValueError:
    print('Mensage 1')
except IndexError:
    print('Mensage 2')
except:
    print('Mensage 3')


# Forma completa para lidar com exceções:
# try:
    # Bloco 1
# except Exception1:
    # Bloco tratador para a exception 1
# except Exception2:
    # Bloco tratador para a exception 1
# ...
# else:
    # Bloco 2 - executado caso nenhuma exceção seja levantada
# finally:
    # Bloco 3 - executado independente do que ocorrer.
# Instrução fora do try/except


