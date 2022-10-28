#Imprime "Hello World" na tela
print("Hello World")

#pergunta seu nome e o imprime na tela
nome = input('Digite seu primeiro nome: \n')
print(nome)

#Pede o seu ano de nascimento e descobre sua idade
anoDeNascimento =  eval(input('Qual o seu ano de nascimento? Digite no formato AAAA: \n'))
idade = 2022 - anoDeNascimento
print(f'Você tem {idade} anos')

# Calcula seu IMC
peso = eval(input('Qual seu peso em kg? '))
altura = eval(input('Qual sua altura em metros (use o ponto (.) ao invés da vírgula (,)?'))
imc = peso/(altura**2)
print(f'Seu IMC é de {imc}')

#Usa diferentes formatações de dados de saída
hora = 10
minutos = 26
segundos = 18
print(str(hora) + ' : ' + str(minutos) + ' : ' + str(segundos))
print('{} : {} : {}'.format(hora, minutos, segundos))
print(f'{hora} : {minutos} : {segundos}')
#largura do campo
print('{:3},{:4}'.format(10, 100))
#largura + valor float com precisão definida
print('{:5.3}'.format(imc))

#imprimindo uma sequência
seq = [1,2,3,4,5,6,7,8,9,10]
print(seq)

#Imprimindo substring
str = 'Hello world!'
print(str[0:4])
print(str[2:8])
print(str[::-1])
print(str[8:2:-1])
