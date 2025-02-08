def texto(msg):
    print('-_' * len(msg))
    print('{:^40}'.format(msg))
    print('-_' * len(msg))
    print('''\nEscolha uma das opções abaixo:\n
1: Comprimento
2: Massa
3: Tempo
4: Área
5: Velocidade
6: Temperatura
7: Moeda
8: Líquido
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
  print(f'\n{metros} (m²) é igual a {metros * 10000} (cm²) \n')

def velocidade():
  km = float(input('\nDigite quantos quilometros por hora você gostaria de converter para metros por segundo: (km/h)'))
  while km <= 0:
    km = float(input('\nErro: não é possível converter quilometros por hora negativo. Digite novamente: (km/h) '))
  print(f'\n{km} (km/h) é igual a {km / 3.6} (m/s) \n')
  
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
