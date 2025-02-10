def texto(msg):
    print('-_' * len(msg))
    print('{:^40}'.format(msg))
    print('-_' * len(msg))
    print('''\nEscolha uma das opções abaixo:\n
1: Comprimento / Tempo / Velocidade / Área
2: Massa / IMC
3: Temperatura / Líquido
4: Moeda / Calculadora
5: Nota simples / Tabuada''')

def menu1():
  print('''\nDigite uma das opções abaixo: \n
1: Comprimento
2: Tempo
3: Velocidade
4: Área ''')

def menu2():
  print('''\nDigite uma das opções abaixo: \n
1: Massa
2: IMC''')

def menu3():
  print('''\nDigite uma das opções abaixo: \n
1: Temperatura
2: Líquido''')
  
def menu4():
  print('''\nDigite uma das opções abaixo: \n
1: Moeda
2: Calculadora''')
  
def menu5():
  print('''\nDigite uma das opções abaixo: \n
1: Nota simples
2: Tabuada  
''')

def comprimento():
  print('''\nDigite uma das opções abaixo:\n
1: Metros (m) para centímetros (cm)
2: Centímetros (cm) para metros (m)''')
  opcao_comprimento = int(input('\nQual a sua escolha? '))
  while opcao_comprimento != 1 and opcao_comprimento != 2:
    opcao_comprimento = int(input('\nErro: digite 1 ou 2: '))
  if opcao_comprimento == 1:
    metros = float(input('\nDigite quantos metros você gostaria de converter para centímetros: (m) '))
    while metros <= 0:
      metros = float(input('\nErro: não é possível converter números negativos. Digite novamente: (m) '))
    print(f'\n{metros:.2f} (m) é igual a {metros * 100:.2f} (cm)\n')
  elif opcao_comprimento == 2:
    centimetros = float(input('\nDigite quantos centímetros você gostaria de converter para metros: (cm) '))
    while centimetros <= 0:
      centimetros = float(input('\nErro: não é possível converter números negativos. Digite novamente: (cm) '))
    print(f'{centimetros:.2f} (cm) é igual a {centimetros / 100:.2f} (m)\n')

def massa():
  print('''\nDigite uma das opções abaixo: \n
1: Quilogramas (kg) para gramas (g)
2: Gramas (g) para quilogramas (kg)''')
  opcao_massa = int(input('\nQual a sua escolha? '))
  while opcao_massa != 1 and opcao_massa != 2:
    opcao_massa = int(input('Erro: digite 1 ou 2: '))
  if opcao_massa == 1:
    quilogramas = float(input('\nDigite quantos quilogramas você gostaria de converter para gramas: (kg) '))
    while quilogramas <= 0:
      quilogramas = float(input('\nErro: não é possível converter quilogramas negativos. Digite novamente: (kg) '))
    print(f'\n{quilogramas:.2f} (kg) é igual a {quilogramas * 1000:.2f} (g) \n')
  elif opcao_massa == 2:
    gramas = float(input('\nDigite quantas gramas você gostaria de converter para kg: (g) '))
    while gramas <= 0:
      gramas = float(input('Erro: não é possível converter gramas negativas. Digite novamente: (g) '))
    print(f'\n{gramas:.2f} (g) é igual a {gramas/1000:.2f} (kg) \n')
  
def tempo():
  print('''\nDigite uma das opções abaixo:\n
1: Horas (h) para minutos (m)
2: Minutos (m) para segundos (s)''')
  opcao_tempo = int(input('\nQual a sua escolha? '))
  while opcao_tempo != 1 and opcao_tempo != 2:
    opcao_tempo = int(input('\nErro: escolha 1 ou 2: '))
  if opcao_tempo == 1:
    horas = int(input('\nDigite quantas horas você gostaria de converter para minutos: (h) '))
    while horas <= 0:
      horas = int(input('\nErro: não é possível converter horas negativas. Digite novamente: (h) '))
    print(f'\n{horas} (h) é igual a {horas*60} (m) \n')
  elif opcao_tempo == 2:
    minutos = int(input('\nDigite quantos minutos você gostaria de converter para segundos: (m) '))
    while minutos <= 0:
      minutos = int(input('\nErro: não é possível converter minutos negativos. Digite novamente: (m) '))
    print(f'\n{minutos} (m) é igual  {minutos* 60} (s) \n')

def area():
  metros = float(input('\nDigite quantos metros quadrados você gostaria de converter para centímetros: (m²) '))
  while metros <= 0:
    metros = float(input('\nErro: não é possível converter metros negativos. Digite novamente: (m²) '))
  print(f'\n{metros:.2f} (m²) é igual a {metros * 10000:.2f} (cm²) \n')

def velocidade():
  km = float(input('\nDigite quantos quilometros por hora você gostaria de converter para metros por segundo: (km/h)'))
  while km <= 0:
    km = float(input('\nErro: não é possível converter quilometros por hora negativo. Digite novamente: (km/h) '))
  print(f'\n{km:.2f} (km/h) é igual a {km / 3.6:.2f} (m/s) \n')
  
def temperatura():
  print('''\nDigite uma das opções abaixo:\n
1: Celsius (ºC) para Fahrenheit (ºF)
2: Fahrenheit (ºF) para Celsius (ºC)''')
  opcao_temperatura = int(input('\nQual a sua escolha? '))
  while opcao_temperatura != 1 and opcao_temperatura != 2:
    opcao_temperatura = int(input('Erro: digite 1 ou 2: '))
  if opcao_temperatura == 1:
    celsius = float(input('\nDigite quantos graus celsius você gostaria de converter para graus fahrenheit: (ºC) '))
    while celsius <= 0:
      celsius = float(input('\nErro: não é possível converter celsius negativo. Digite novamente: (ºC) '))
    print(f'\n{celsius:.2f} ºC é igual a {(celsius * 1.8) + 32:.2f} ºF \n')
  if opcao_temperatura == 2:
    fahrenheit = float(input('\nDigite quantos graus fanhrenheit você gostaria de converter para graus celsius: (ºF) '))
    while fahrenheit <= 0:
      fahrenheit = float(input('\nErro: não é possível converter graus fahrneheit negativo. Digite novamente: (ºF) '))
    print(f'\n{fahrenheit:.2f} ºF é igual a {(fahrenheit - 32) / 1.8:.2f} ºC \n')

def moedas():
  print('''\nCotação do dólar: R$ 1.00 = US$ 5.85
Cotação do euro: R$ 1.00 = EUR 6.40\n
Digite uma das opções abaixo: \n
1: Real - Dólar
2: Dólar - Real
3: Real - Euro
4: Euro - Real''')
  opcao_moedas = int(input('\nQual a sua escolha? '))
  while opcao_moedas <1 or opcao_moedas >4:
    opcao_moedas = int(input('\nErro: digite de 1 a 4: '))
  if opcao_moedas == 1:
    real = float(input('\nDigite quantos reais você gostaria de converter para dólar: R$ '))
    while real <= 0:
      real = float(input('\nErro: não é possível converter valores negativos. Digite novamente: R$ '))
    print(f'\nR$ {real:.2f} é igual a US$ {real * 0.17:.2f}\n')
  elif opcao_moedas == 2:
    dolar = float(input('\nDigite quantos dólares você gostaria de converter para real: US$ '))
    while dolar <= 0:
      dolar = float(input('\nErro: não é possível converter valores negativos. Digite novamente: US$  '))
    print(f'\nUS$ {dolar:.2f} é igual a R$ {dolar * 5.85:.2f} \n')
  elif opcao_moedas == 3:
    real = float(input('\nDigite quantos reais vocêe gostaria de converter para euro: R$ '))
    while real <= 0:
      real = float(input('\nErro: não é possível converter valores negativos. Digite novamente: R$ '))
    print(f'\nR$ {real:.2f} é igual a EUR {real * 0.16:.2f} \n')
  elif opcao_moedas == 4:
    euro = float(input('\nDigite quantos euros você gostaria de converter para real: EUR '))
    while euro <= 0:
      euro = float(input('\nErro: não é possível converter valores negativos. Digite novamente: '))
    print(f'\nEUR {euro:.2f} é igual a R$ {euro * 6.40:.2f} \n')

def liquido():
  print('''\nDigite uma das opções abaixo:\n
1: Litros (l) para mililitros (ml)
2: Mililitros (ml) para Litros (l)
        ''')
  opcao_liquido = float(input('\nQual a sua escolha? '))
  while opcao_liquido != 1 and opcao_liquido != 2:
    opcao_liquido = float(input('\nErro: digite 1 ou 2: '))
  if opcao_liquido == 1:
    litros = float(input('\nDigite quantos litros você gostaria de converter para mililitros: (l) '))
    while litros <= 0:
      litros = float(input('\nErro: não é possível converter litros negativos. Digite novamente: '))
    print(f'\n{litros:.2f} (l) é igual a {litros*1000:.2f} (ml) \n')
  elif opcao_liquido == 2:
    mililitros = float(input('\nDigite quantos mililitros você gostaria de converter para litros: (ml) '))
    while mililitros <= 0:
      mililitros = float(input('\nErro: não é possível converter mililitro negativo. Digite novamente: '))
    print(f'\n{mililitros:.2f} (ml) é igual a {mililitros/1000:.2f} (l) \n')
  
def imc():
  print('''\nEis as faixas de IMC: \n
- Abaixo de 18,5: Abaixo do peso
- Entre 18,5 e 24,9: Peso normal
- Entre 25,0 e 29,0: Sobrepeso
- Entre 30,0 e 34,9: Obesidade grau 1
- Entre 35,0 e 39,9: Obesidade grau 2
- Acima de 4,0: Obesidade grau 3 (mórbida)''')
  peso = float(input('\nDigite o seu peso: (kg) '))
  while peso <= 0:
    peso = float(input('\nErro: não é possível calcular o imc de peso negativo. Digite novamente: '))
  altura = float(input('\nDigite a sua altura: (m) '))
  while altura <= 0 and altura > 2.50:
    altura = float(input('\nErro: digite novamente: '))
  imc = peso / (altura ** 2)
  if imc < 18.5:
    print(f'\nSeu IMC é: {imc:.2f} e você está abaixo do peso!')
  elif imc >= 18.5 and imc <= 24.9:
    print(f'\nSeu IMC é: {imc:.2f} e você está com o peso normal!')
  elif imc >= 25 and imc <= 29.9:
    print(f'\nSeu IM é: {imc:.2f} e você está com sobrepeso!')
  elif imc >= 30 and imc <= 34.9:
    print(f'\nSeu IMC é: {imc:.2f} e você está com obesidade grau 1!')
  elif imc >= 35 and imc <= 39.9:
    print(f'\nSeu IMC é: {imc:.2f} e você está com obesidade grau 2!')
  elif imc >= 40:
    print(f'\nSeu IMC é: {imc:.2f} e você está com obesidade grau 3 (mórbida)!')
def calculadora():
  print('''\nEscolha uma das opções abaixo:\n
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão''')
  opcao = int(input('\nDigite uma opção: '))
  while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
    opcao = int(input('\nErro: digite novamente: '))
  num1 = float(input('\nDigite o 1º número: '))
  while num1 == 0:
    num1 = int(input('\nNão é possível fazer cálculos com 0. Digite outro número: '))
  num2 = float(input('\nDigite o 2º número: '))
  while num2 == 0:
    num2 = int(input('\nNão é possível fazer cálculos com 0. Digite outro número: '))
  if opcao == 1:
    print(f'\n{num1} + {num2} = {num1 + num2:.2f}')
  elif opcao == 2:
    print(f'\n{num1} - {num2} = {num1 - num2:.2f}')
  elif opcao == 3:
    print(f'\n{num1} x {num2} = {num1 * num2:.2f}')
  elif opcao == 4:
    print(f'\n{num1} / {num2} = {num1 / num2:.2f}')

def notas():
    nome = input('\nDigite o nome do aluno: ')
    while nome == '' :
        nome = input('\nErro: digite um nome: ')
    nota1 = float(input('\nDigite a 1ª nota: '))
    while nota1 > 10 or nota1 < 0:
        nota1 = float(input('\nErro: não é possível uma nota ter esse valor. Digite novamente: '))
    nota2 = float(input('\nDigite a 2ª nota: '))
    while nota2 > 10 or nota2 < 0:
        nota2 = float(input('\nErro: não é possível uma nota ter esse valor. Digite novamente: '))
    nota3 = float(input('\nDigite a 3ª nota: '))
    while nota3 > 10 or nota3 < 0:
        nota3 = float(input('\nErro: não é possível uma nota ter esse valor. Digite novamente: '))
    media = ((nota1 + nota2 + nota3) / 3)
    media_nota(nome, media)

def media_nota(nome, media):
    if media >= 6:
        print(f'\nO aluno {nome} foi aprovado com média final: {media:.2f}!')
    else:
        pontos = 6 - media
        print(f'\nO aluno {nome} foi reprovado com média final: {media:.2f} e precisou de {pontos:.2f} para passar.')
  
def tabuada():
  num = int(input('\nDigite um número para ver sua tabuada: '))
  while num == 0:
    num = int(input('\nErro: não há tabuada do zero. Digite um outro número: '))
  limite = int(input('\nDigite até que número você gostaria de ver a tabuada: '))
  print('\n')
  i = 0
  while i <= limite:
    print(f'{num} x {i} = {num * i}')
    i += 1