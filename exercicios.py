#1
#Elabore um processo lógico (i.e. algoritmo) para mudar um pneu furado de um carro
#qualquer. Admita que estejam disponíveis um macaco e outro pneu em boas
#condições.

n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))
p = n1*n2
print ("O produto é:", p)

#2
#Faça um algoritmo que leia uma temperatura em graus Fahrenheit e converta e
#mostre em graus Centígrados.

f = float(input("Insira a temperatura em Fahrenheit: "))
c = (f - 32) * 5/9
print ("A temperatura em Centígrados é:", c)

#3
#Faça um algoritmo que leia uma temperatura em graus Fahrenheit e converta e
#mostre em graus Centígrados.

c = float (input("Insira a quantidade de chuva em polegadas: "))
mm = (c*25.4)
print ("Em mm, choveu um total de:", mm)

#4
#Um sistema de equações lineares da forma:
#ax + by =c
#dc + ey = f
#pode ser resolvido utilizando-se as seguintes fórmulas:
# x= ce-bf/ae-bd
# y= af-cd/ae-bd
#Faça um algoritmo que leia os valores a, b, c, d, e, f, e calcule x e y.

a = float(input("Insira o valor a: "))
b = float(input("Insira o valor b: "))
c = float(input("Insira o valor c: "))
d = float(input("Insira o valor d: "))
e = float(input("Insira o valor e: "))
f = float(input("Insira o valor f: "))

x = (c*e)-(b*f)/(a*e)-(b*d)
y = (a*f)-(c*d)/(a*e)-(b*d)

print ("O valor de x é igual a:", x)
print ("O valor de y é igual a:", y)

#5 
#O governador acaba de liberar R$ 1.000.000.000,00 para construção de casas
#populares. Cada casa custa o equivalente a 90 salários mínimos. Faça um algoritmo
#que leia o valor do salário mínimo e calcule a quantidade de casas que podem ser
#construídas com o recurso liberado.

s = float(input("Insira o valor do salário mínimo: "))
valorcasa = s*90
quantidadecasa= 1000000000/valorcasa

print("Com este valor de salário mínimo, pode-se construir", round(quantidadecasa), "casas" )

#6
#Faça um algoritmo que calcule o volume de uma lata de óleo. Escreva o resultado.
#FÓRMULA: volume = p * raio2 * altura

r = float(input("Em cm, insira o valor do raio da lata: "))
a = float(input("Em cm, insira o valor da altura da lata: "))
v = 3.14*(r*r)*a 


print("O volume da lata é igual a: {}cm3".format(round(v, 2)))