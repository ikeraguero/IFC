#1
#Faça uma função para converter uma temperatura em graus Fahrenheit para
#Celsius. A temperatura em Fahrenheit é o dado de entrada e a temperatura em
#Celsius é o dado de saída. Utilize a fórmula C = (F - 32) * 5/9, onde F é a
#temperatura em Fahrenheit e C é a temperatura em Celsius.

def converte(F):
  result = (F - 32) * 5 / 9
  return result
C = converte(68)
print(C)

#2
#Crie uma função que realize a conversão de Polegadas (pol) para Centímetros
#(cm), onde pol é passado como parâmetro e cm é retornado. Sabe-se que 1
#polegada tem 2.54 centímetros. Crie também um programa para testar tal função.

def p_cm (p, cm):
    cm = p*2.54
    print("É igual a {}cm".format(cm))
    p = int(input("Insira o valor em polegadas: "))
    p_cm(p, cm) 

#3
#Escreva uma função que receba um número inteiro e imprima o mês
#correspondente ao número. Por exemplo, 2 corresponde a “fevereiro”. O
#procedimento deve mostrar uma mensagem de erro caso o número recebido não
#faça sentido. Gere também um programa que leia um valor e chame a função
#criada.

def calendario(num):
  if(num == 1):
    print("Janeiro")
  elif(num == 2):
    print("Fevereiro")
  elif(num == 3):
    print("Março")
  elif(num == 4):
    print("Abril") 
  elif(num == 5):
    print("Maio") 
  elif(num == 6):
    print("Junho") 
  elif(num == 7):
    print("Julho") 
  elif(num == 8):
    print("Agosto") 
  elif(num == 9):
    print("Setembro") 
  elif(num == 10):
    print("Outubro") 
  elif(num == 11):
    print("Novembro") 
  elif(num == 12):
    print("Dezembro")     
  else:
    print("Mês inválido, informe um valor de 1 a 12.")

mes = int(input("Número: "))
calendario(mes)

#4
#Escreva uma função que receba um número natural e imprima os três primeiros
#caracteres do dia da semana correspondente ao número. Por exemplo, 7
#corresponde a “SAB”. O procedimento deve mostrar uma mensagem de erro caso
#o número recebido não corresponda a um dia da semana. Gere também um
#programa que utilize essa função, chamando-a, mas antes lendo um valor para
#passagem de parâmetro.

def semana(num):
  if(num == 1):
    print("DOM")
  if(num == 2):
    print("SEG")
  if(num == 3):
    print("TER")
  if(num == 4):
    print("QUA")
  if(num == 5):
    print("QUI")
  if(num == 6):
    print("SEX")
  if(num == 7):
    print("SAB")
  if(num > 7 or num < 1):
    print("Dia inválido, informe um valor entre 1 e 7.")

dia = int(input("Número: "))
semana(dia)

#5
#Escreva uma função que receba um número natural e imprima os três primeiros
#caracteres do dia da semana correspondente ao número. Por exemplo, 7
#corresponde a “SAB”. O procedimento deve mostrar uma mensagem de erro caso
#o número recebido não corresponda a um dia da semana. Gere também um
#programa que utilize essa função, chamando-a, mas antes lendo um valor para
#passagem de parâmetro.

def divisivel(x, y):
    if x % y == 0:
        print("1")
    else:
        print("0")
x = int(input("Informe o valor de x: "))
y = int(input("Informe o valor de y: "))
divisivel(x, y)

#6
#Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
#1-feminino 2-masculino) de uma pessoa. Depois faça uma função chamada
#pesoideal que receba a altura e o sexo via parâmetro e que calcule e retorne seu
#peso ideal, utilizando as seguintes fórmulas:
#• para homens: (72.7 * h) – 58
#• para mulheres: (62.1 * h) – 44.7
#Observação: Altura = h (na fórmula acima).

def pesoideal(sexo, altura):
  if sexo == 1:
    femenino = (62.1 * altura) - 44.7
    print("Peso desta mulher é de {}kg".format(round(femenino, 2)))
  if sexo == 2:
    masculino = (72.7 * altura) - 58 
    print("Peso deste homem é de {}kg".format(round(masculino, 2)))
 
sexo = int(input("Digite [1] para mulher e [2] para homem: "))
h = float(input("Informe a altura: "))
pesoideal(h, sexo)

#7
#Faça uma função que calcule a hipotenusa. Os catetos são os dados de entrada e
#a hipotenusa é o dado de saída.
import math

def pitagoras (a, b):
    hipotenusa = a ** 2 + b **2
    hipotenusa = math.sqrt(hipotenusa)
    print("O valor da hipotenusa é {}".format(hipotenusa))

c1 = float(input("Insira o valor do 1º cateto: "))
c2 = float(input("Insira o valor do 2º cateto: "))
pitagoras(c1, c2)

#8
#Escreva um programa para ler as notas das duas avaliações de um aluno no
#semestre. Faça uma função que receba as duas notas por parâmetro e calcule e
#escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!”
#somente se o aluno foi aprovado (considere 6.0 a média mínima para aprovação).

def nota (n1, n2):
    media = (n1 + n2) / 2
    if media >= 6:
        print("PARABÉNS! Você foi aprovado.")
    else:
        print("Você foi reprovado.")

n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
nota(n1, n2)