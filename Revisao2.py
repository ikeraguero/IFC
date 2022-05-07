#1
#Ler um valor e escrever se é positivo, negativo ou zero.

n = float(input("Insira um número: "))

if n < 0:
    print("O valor {} é negativo.".format(n))
if n == 0:
    print("O valor {} é igual a 0".format(n))
else:
    print("O valor {} é positivo".format(n))

#2 
#Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10,
#caso contrário escrever NÃO É MAIOR QUE 10!

n = float(input("Informe um número: "))

if n>10:
    print("O número {} é maior do que 10.".format(n))
if n==10:
    print("O número é igual a 10.")
else:
    print("O número {} é menor do que 10.".format(n))

#3 
#Calcule a soma de dois números, se o resultado for maior que 10, mostre-o na tela.

n = float(input("Informe o primeiro valor: "))
n2= float(input("Informe o segundo valor: "))
s = n+n2

if s >10:
    print( "A soma dos dois valores é igual a {}".format(s))
else:
    print("O valor inserido é menor do que 10")

#4
#Entrar com um número e informar se ele é divisível por 5.

n = float(input("Informe um número: "))
d = n % 5

if d == 0:
    print("O número {} é divisível por 5".format(n))
else:
    print("O número {} não é divisível por 5".format(n))

#5
#Construir um algoritmo que indique se o número digitado está entre 20 e 90 ou não.

n = float(input("Informe um número: "))
if n >= 20 and n <=90:
    print("O número {} está entre 20 e 90".format(n))
else:
    print("O número {} não está entre 20 e 90".format(n))

#6
#Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que
#diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a
#pessoa nasceu).

a = int(input("Informe o seu ano de nascimento: "))
i = 2022 - a

if i>=16:
    print("Você tem {} anos, portanto poderá votar esse ano".format(i))
else:
    print("Você tem {} anos, portanto ainda não poderá voltar esse ano".format(i))

#7
#Entrar com o ano de nascimento de uma pessoa e imprimir a idade dela. Verificar se o
#ano digitado é válido.

a = int(input("Informe o seu ano de nascimento: "))
i = 2022 - a
if a < 1 or a > 2022:
    print("O ano inserido é invalido")
else:
    print("Você tem {} anos".format(i))

#8 
#Entrar com a idade de uma pessoa e exibir a mensagem; Maior de idade, menor de
#idade ou acima de 65 anos.

a = int(input("Informe o seu ano de nascimento: "))
if a >= 18 and a < 65:
    print("Maior de idade")
if a < 18:
    print("Menor de idade")
else:
    print("Idoso")

#9
#Ler as notas da 1a e 2a  avaliações de um aluno. Calcular a média aritmética simples e
#escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que se a
#nota for igual ou maior que 6 o aluno é aprovado). Escrever também a média
#calculada.

a = float(input("Informe a primeira nota "))
b = float(input("Informe a segunda nota "))
m = (a + b) / 2

print("A média final foi igual a {}".format(m))
if m >= 6:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado")

#10
#Escrever um algoritmo para ler duas notas de um aluno e escrever na tela a palavra
#“Aprovado” se a média das duas notas for maior ou igual a 7,0. Caso a média seja
#inferior a 7,0, o programa deve ler a nota do exame e calcular a média final. Se esta
#média for maior ou igual a 5,0, o programa deve escrever “Aprovado”, caso contrário
#deve escrever “Reprovado”.

a = float(input("Informe a primeira nota "))
b = float(input("Informe a segunda nota "))
m = (a + b) / 2

if m >= 7:
    print("Aluno aprovado")
else:
    print("Você foi reprovado, faça o exame: ")
    e = float(input("Insira a nota do exame: "))
    mn = (a + b + e) /3
    if mn >=5:
        print("Você foi aprovado")
    else:
        print("Você foi reprovado")

#11 
#Faça um algoritmo que leia um número inteiro e mostre uma mensagem indicando se
#este número é par ou ímpar.

n = int(input("Insira um número inteiro: "))
d = n % 2

if d == 0:
    print("O número {} é par".format(n))
else:
    print("O número {} é ímpar".format(n))

#12
#Ler o nome de 2 times e o número de gols marcados na partida. Escrever o nome do
#vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.

t1 = input("Informe o nome do primeiro time: ")
t2 = input("Informe o nome do segundo time: ")
g1 = int(input("Quantidade de gols do primeiro time: "))
g2 = int(input("Quantidade de gols do segundo time: "))

if g1 == g2:
    print("O jogo entre {} e {} terminou empatado".format(t1, t2))
if g1 > g2:
    print("{} venceu a partida".format(t1))
if g1 < g2:
    print ("{} venceu a partida".format(t2))

#13
#Ler 2 valores (considere que não serão lidos valores iguais) e escrever o maior deles.

n1 = int(input("Informe um número: "))
n2 = int(input("Informe outro número: "))

if n1 == n2:
    print("Resultado indisponível pois os números são iguais")
if n1 > n2:
    print("Entre {} e {}, {} é o maior número".format(n1, n2, n1))
if n1 < n2:
    print("Entre {} e {}, {} é o maior número".format(n1, n2, n2))

#14
#Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma
#dos 2 maiores.

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))

if n1 > n2 and n2 > n3:
    s= n1+n2
    print ("A soma dos dois maiores é igual a {}".format(s))
if n2 > n1 and n1>n3:
    s=n1+n2
    print ("A soma dos dois maiores é igual a {}".format(s))
if n3 > n1 and n1 >n2:
    s=n3+n1
    print ("A soma dos dois maiores é igual a {}".format(s))
if n1 > n3 and n3 >n2:
    s=n3+n1
    print ("A soma dos dois maiores é igual a {}".format(s))

#15
#Faça um algoritmo para calcular o reajuste salarial de um funcionário, de acordo com
#os critérios abaixo:
#• se salário é inferior a R$ 10.000,00 deve ter um reajuste de 55%
#• se salário está entre R$ 10.000,00 (inclusive) e R$ 25.000,00 (inclusive) deve ter um reajuste de 20%
#• se salário é superior a R$ 25.000,00 deve ter um reajuste de 20%.

salario = input(int("Insira o salário do funcionario: "))
if salario < 10000:
    print("Com o reajuste, o salário passará a ser de {}".format(salario + (salario*0,55)))
if salario >= 10000 and salario <= 25000:
    print("Com o reajuste, o salário passará a ser de {}".format(salario + (salario*0,20)))
if salario > 25000:
    print("Com o reajuste, o salário passará a ser de {}".format(salario + (salario*0,20)))