def msg(texto):
    '''Printa na tela uma mensagem personalizada'''
    print('-_' * len(texto))
    print("{:^40}".format(texto))
    print('-_' * len(texto))

def menu():
    '''Retorna a conversão da moeda de acordo com a opção escolhida'''
    opcao = int(input('Qual a sua escolha? '))
    if opcao == 1:
        real = float(input('\nQuantos reais você tem para converter em dólar? R$ '))
        print(f'\nR$ {real:.2f} equivale a US$ {real * 0.17:.2f}')
    elif opcao == 2:
        dolar = float(input('\nQuantos dólares você tem para converter em real: US$ '))
        print(f'\nUS$ {dolar:.2f} equivale a R$ {dolar * 5.85:.2f}')
    elif opcao == 3:
        real = float(input('\nQuantos reais você tem para converter em euro? R$ '))
        print(f'\nR$ {real:.2f} equivale a EUR {real * 0.16:.2f}')
    elif opcao == 4:
        euro = float(input('\nQuantos euros você tem para converter em real? EUR '))
        print(f'\nEUR {euro:.2f} equivale a R$ {euro * 6.40:.2f}')
    else:
        print('Opção inválida!')