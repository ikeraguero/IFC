#1
#Faça um algoritmo que:
#• leia 20 números inteiros;
#• escreva os números que são negativos;
#• escreva a média dos números positivos.

s = 0
contapos = 0
for i in range (5):
    n = int(input("Insira um número inteiro: "))
    if n < 0:
        print("{} é negativo".format(n))
    else:
        s = s + n
        contapos = contapos +1
        media = s/contapos
print ("A média dos números positivos é {}".format(media))

#2
#Faça um algoritmo que leia 15 números inteiros e escreva, para cada número lido, se é par ou ímpar.
  

for i in range (15):
    n = int(input("Insira um numero inteiro:"))
    if n % 2 == 0:
        print("O número {} é par".format(n))
    else:
        print("O número {} é impar".format(n))
    
#3
# Faça um algoritmo que leia a altura de 20 pessoas e calcule a média aritmética das alturas.

s = 0
q = 0
for i in range (5):
    a = int(input("Insira a altura de uma pessoa em cm: "))
    q = q + 1
    s = s + a
    m = s / q
print("A média de altura é de {}".format(m))    
    
#4
#Faça um algoritmo que leia n valores inteiros e escreva quantos desses valores são negativos.

negativos = 0
n = 0
for i in range (10):
    n = int(input("Insira um numero inteiro: "))
    if n < 0:
        negativos = negativos + 1
print("Foram inseridos {} números negativos".format(negativos))

#5
#Faça um algoritmo que calcule e escreva a soma dos números pares e a soma dos números ímpares entre 1 e 100.

sp = 0
si = 0

for i in range (1, 101):
    if i % 2 == 0:
        sp = sp + i
    else:
        si = si + i
print ("Entre 1 e 100, a soma dos pares é igual a {} e a soma dos impares é igual a {}".format(sp, si))

#6
#Construir um algoritmo que calcule o fatorial de um número N.

n = int(input("Fatorial de: ") )
r=1
for n in range(1,n+1):
    r *= n

print("O fatorial de {} é {}.".format(n,r))

#7 
#Faça um algoritmo que calcule e escreva a soma da seguinte série de 100 termos:
#1 + 2 + 3 + 4... 100

s = 0
for i in range (101):
    s= s+i
    print("{} + {} = {}".format(s-i, i, s))
print ("A soma dos números de 1 à 100 é igual a {}".format(s))

#8
#Um hotel cobra R$ 50,00 de diária por hóspede e mais uma taxa de serviços. A taxa de
#serviços é de:
#• R$ 7,50 por diária, caso o número de diárias seja menor que 15;
#• R$ 6,50 por diária, caso o número de diárias seja igual a 15;
#• R$ 5,00 por diária, caso o número de diárias seja maior que 15.
#Faça um algoritmo que apresente as seguintes opções ao recepcionista:
#1. encerrar a conta de um hóspede
#2. verificar número de contas encerradas
#3. finalizar a execução
#Caso a opção escolhida seja a primeira, leia o nome e o número de diárias do hóspede
#e escreva o nome e total a ser pago. Caso a opção escolhida seja a segunda, informe o
#número de hóspedes que deixaram o hotel (número de contas encerradas).

print ("[1] Encerrar a conta de um hóspede ")
print ("[2] Verificar número de contas encerradas")
print ("[3] Finalizar a execução")
for i in range(5):
    n = int(input("Selecione a opção desejada: "))
contasencerradas = 0
if n == 1:
    contasencerradas = contasencerradas + 1
    nome = input("Insira o nome do hóspede: ")
    diarias = int(input("Insira o total de diárias: "))
    if diarias < 15:
        total = (50*diarias) + (7.5*diarias)
        print ("O hóspede {} deve pegar um valor total de R${}".format(nome, round(total, 2)))
    if diarias == 15:
        total = (50*diarias) + (6.5*diarias)
        print ("O hóspede {} deve pegar um valor total de R${}".format(nome, round(total, 2)))
    if diarias > 15:
        total = (50*diarias) + (5*diarias)
        print ("O hóspede {} deve pegar um valor total de R${}".format(nome, round(total, 2)))
if n == 2:
    print ("Até o momento, {} contas foram encerradas".format(contasencerradas))
if n ==3:
    print("EXECUÇÃO FINALIZADA, SAINDO DO PROGRAMA...")

#9
#Uma loja de departamentos oferece para seus clientes um determinado desconto de
#acordo com o valor da compra efetuada. O desconto é de 20% caso o valor da compra
#seja maior que R$ 500,00 e de 15% caso seja menor ou igual. Faça um algoritmo que
#leia, para cada cliente, nome, endereço e valor da compra e escreva o total a pagar.
#Um nome de cliente igual a ULTIMO indica o fim da entrada de dados.

n = ""
while n != "ultimo":
    n = str(input("Nome: "))
    e = str(input("Endereço: "))
    valorcompra = int(input("Valor da compra: "))

    if valorcompra > 500:
        desconto = (valorcompra * 20) / 100
        valorcompra = valorcompra - desconto

    if valorcompra < 500:
        desconto = (valorcompra * 15) / 100
        valorcompra = valorcompra - desconto
    print ("{}. Endereço: {}. Valor da compra com desconto: R${}".format(nome, e, valorcompra))
print("Fim do programa")

#10
#Os regulamentos de uma competição de pesca impõem um limite no peso total de
#pesca de um dia. Faça um algoritmo que leia o limite diário (em quilogramas) e então
#leia o peso (em gramas) de cada peixe e escreva o peso total da pesca obtido até
#aquele ponto. Quando o limite diário for excedido escreva uma mensagem e encerre a
#execução do algoritmo. O algoritmo deve ainda apresentar ao usuário a seguinte
#mensagem: informar o peso de mais um peixe: s (SIM) / n (NÃO)? antes de prosseguir
#com a entrada de dados.

r = "s"
speixes = 0
limite_diario = int(input("Limite diário em kg: "))
while r == "s":
    ppeixe = int(input("Peso do peixe em g: "))
    ppeixe = ppeixe / 1000
    speixes = speixes + ppeixe
    if ppeixe > limite_diario:
        print("Peso do peixe superior ao limite diário")
    elif speixes > limite_diario:
        print("Limite diário atingido")
    else:
        print("A soma atual dos peixes: {}g".format(speixes))
    r = str(input("Deseja digitar mais um valor? Digite 'sim' ou 'não'. "))
print("Peso dos peixes: {}kg".format(speixes))

#11
#Faça um algoritmo que leia n pares de valores, sendo o primeiro valor o número de
#inscrição do atleta e o segundo a altura (em cm) do atleta. Escreva:
#• o número de inscrição e a altura do atleta mais alto;
#• o número de inscrição e a altura do atleta mais baixo;
#• a altura média do grupo de atletas.

contagem_altura = 0
soma_alturas = 0
menor = maior = 0
quantidade = 0
while contagem_altura <= 5:
    inscr = int(input("Informe a inscrição do atleta: "))
    altura = int(input("Informe a altura do atleta: "))
    contagem_altura = contagem_altura + 1
    soma_alturas = soma_alturas + altura
    media = soma_alturas / contagem_altura
    quantidade = quantidade + 1
    if quantidade ==1:
        maior = menor = altura
    else:
        if altura > maior:
            maior = altura
        if altura < menor:
            menor = altura
print("A média é {}. Maior altura: {}. Menor altura: {}.".format(media, maior, menor))

#12 
#Faça um algoritmo que calcule e imprima os valores de y, onde:
#y = (3 + 2x + 6x^2) / 1+9x +16x^2) , para x variando de 1.0 até 5.0, em intervalos de 0.1 unidades.

x = 1
while x <= 5:
    y = (3 + (2 * x) + 6 * x ** 2) / (1 + (9 * x) + 16 * x ** 2)
    x = x + 0.1
    y = round(y,6)
    print("y = {}".format(y))

#13
#Faça um algoritmo que leia n números inteiros e escreva, para cada número lido, os
#divisores e quantidade de divisores.
# #EXEMPLO: número lido = 12
# divisores = 1, 2, 3, 4, 6, 12
# quantidade divisores = 6

divisores = 1
cont_div = 1
num = int(input("Informe um valor: "))
while divisores <= num:
    if num % divisores == 0:
        print("Número lido: {}. Divisores: {}. Quantidade de divisores: {}".format(num, divisores, cont_div))
        cont_div = cont_div +1
    divisores = divisores + 1

#14
#Faça um algoritmo que leia a quantidade de tinta que uma caneta, e enquanto a
#caneta tiver tinta para escrever, escreva “Enquanto tem tinta a caneta escreve...”.
#Considere que a cada comando de escrita a caneta gasta 2% da tinta que possui.
tinta = 0
while tinta <= 100:
    print("Enquanto tem tinta a caneta escreve...")
    tinta = tinta + 2
    if tinta == 100:
        print("Acabou a tinta da caneta.")

#15
#Faça um algoritmo que leia valores, sendo que cada valor representa a idade de uma
#pessoa. Calcule e escreva a idade média do grupo de pessoas. Só devem ser
#computados no cálculo valores maiores do que zero. O algoritmo deve apresentar ao
#usuário a seguinte mensagem:
#deseja digitar mais um valor: s (SIM) / n (NAO)?,
#antes de prosseguir com a entrada de dados.

r = "sim"
s = 0
contidade = 0
while r == "s":
    idade = int(input("Idade: "))
    if idade == 0:
        print("Valor inválido")
    else:
        s= s + idade
        contidade = contidade + 1
        media = s / contidade
    r = str(input("Deseja digitar mais um valor? Digite 'sim' ou 'não'. "))
print("A média de idades é: {}".format(media))