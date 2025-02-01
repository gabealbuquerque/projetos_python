# Este é o conversor-de-dolar-e-euro nº 1 (mais simples).
# Há também o conversor nº 2, sendo mais completo (possuindo funções, loops, tratamento de erro, e etc...)
print('Bem vindo ao Conversor de Moedas')
print('''1: Real - Dólar
2: Dólar - Real
3: Real - Euro
4: Euro - Real''')
menu = int(input('Digite sua opção: '))
if menu == 1:
    real = float(input('Quantos reais você tem para converter em dólar? R$ '))
    print(f'R$ {real:.2f} = US$ {real * 0.17:.2f}')
elif menu == 2:
    dolar = float(input('Quantos dólares você tem para converter em real? US$ '))
    print(f'US$ {dolar:.2f} = R$ {dolar * 5.85:.2f}')
elif menu == 3:
    real = float(input('Quantos reais você tem para converter em euro? R$ '))
    print(f'R$ {real:.2f} = EUR {real * 0.16:.2f}')
elif menu == 4:
    euro = float(input('Quantos euros você tem para converter em real? EUR '))
    print(f'EUR {euro:.2f} = R$ {euro * 6.40}')
else:
    print('Opção inválida!')
print('Obrigado e volte sempre!')
