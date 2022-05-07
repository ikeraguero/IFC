#1
#Inicializar um vetor de inteiros com números de 0 a 99.

lista = list(range(100))
print(lista)

#2
#Escreva um algoritmo que leia um conjunto de 10 notas, armazene-as em uma variável
#composta chamada NOTA e calcule e imprima a sua média.

nota = []
soma = 0
for i in range(10):
    nota.append(float(input("Insira a nota: ")))
    soma = soma + nota[i]
media = soma/10

print("A média das notas é de {}".format( media))

#3
#Repita o algoritmo acima, porém imprima quantos valores estão acima da média.

nota = []
soma = 0
acima = []
for i in range(10):
    nota.append(float(input("Insira a nota: ")))
    soma = soma + nota[i]
media = soma/10
for item in nota:
    if item >= media:
        acima.append(item)

print("A média das notas é de {}".format( media))
print("{} notas estão acima da média".format(len(acima)))

#4
#Faça um algoritmo que leia um vetor que contém as notas de 30 alunos. Imprima o maior
#valor, o menor valor, a média da turma e a quantidade de notas abaixo da média.

notas = []
soma = 0
for item in range(10):
    notas.append(float(input("Nota: ")))
    soma = soma + notas[item]
    media = soma / 10
maior = notas[0]
menor = notas[0]
for i in notas:
    if i > maior:
        maior = i
    elif i < menor:
        menor = i
abaixomedia = 0
for item in range(10):
    if notas[item] <= media:
        abaixomedia = abaixomedia + 1
for i in range(len(notas)):
    print("A menor nota foi de {}, a maior de {}, a média foi {}. Houveram {} notas abaixo da média.".format(menor, maior, media, abaixomedia ))

#5
#Escreva um algoritmo que leia um vetor de 200 valores numéricos reais e os imprima na
#ordem contrária em que foi lida.

num = list(range(200))
num = sum(num)
print(num)

#6
#Classificar um vetor numérico VET de 20 elementos em ordem crescente.

lista = []
for item in range(20):
    lista.append(int(input("Número: ")))
    lista.sort()
print(lista)

#7
#Faça um algoritmo que leia um conjunto de 10 elementos reais e os coloque em um vetor.
#Construa um segundo vetor formado da seguinte maneira:
#• Os elementos de ordem par são os correspondentes do primeiro vetor multiplicados por 3.
#• Os elementos de ordem ímpar são os correspondentes do primeiro vetor divididos por 2.
#• Imprima os dois vetores.

l = []
l1 = []
for item in range(10):
    l.append(float(input("Número: ")))   
for num in l:
    if num % 2 == 0:
        num = num * 3
        l1.append(num)
    elif num % 2 == 1:
        num = num / 2
        l1.append(num)
print("1º vetor: {}. 2º vetor: {}".format(l, l1))

#8
#Escreva um algoritmo para fazer a soma de dois vetores de 10 elementos reais lidos do
#teclado. O primeiro elemento do primeiro vetor deverá ser adicionado ao primeiro elemento do
#segundo vetor e, o resultado deverá ser acumulado em um terceiro vetor também de 10
#elementos. Imprimir os três vetores conforme layout de impressão abaixo:
#VETOR 1: __ __ __ __ __ __ __ __ __ __
#VETOR 2: __ __ __ __ __ __ __ __ __ __
#VETOR 3: __ __ __ __ __ __ __ __ __ __

v1 = []
v2 = []
v3 = []
for i in range(10):
    v1.append(int(input("Números do primeiro vetor: ")))
    v2.append(int(input("Números do segundo vetor: ")))

    num = v1[i] + v2[i]
    v3.append(num)
print("1º vetor: {}. 2º vetor: {}. 3º vetor: {}".format(v1,v2, v3))

#9
#Fazer um algoritmo que calcule e escreva o somatório dos valores armazenados numa variável
#composta unidimensional (vetor) A, de 100 elementos numéricos a serem lidos do dispositivo
#de entrada.

n = list(range(100))
n = sum(n)
print(n)

#10
#Fazer um algoritmo que:
#a) Leia duas variáveis compostas unidimensionais, contendo, cada uma, 25 elementos numéricos;
#b) intercale os elementos desses dois conjuntos formando uma nova variável composta
#unidimensional de 50 elementos;
#c) Escreva o resultado obtido.

l1 = []
l2 = []
for i in range(25):
    l1.append(float(input("Valor para a primeira lista: ")))
    l2.append(float(input("Valor para a segunda lista: ")))
    l3 = list(l1 + l2)
    l3[::2] = l1
    l3 [1 :: 2] = l2
print(l3)