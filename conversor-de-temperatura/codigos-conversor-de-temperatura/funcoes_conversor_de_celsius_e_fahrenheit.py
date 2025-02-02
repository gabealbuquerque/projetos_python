def msg(texto):
    print('-_' * len(texto))
    print('{:^49}'.format(texto))
    print('-_' * len(texto))

def menu():
    print('''\nEscolha uma das opções
\n1: Celsius - Fahrenheit
2: Fahrenheit - Celsius''')
    opcao = int(input('\nQual opção você escolhe? '))
    while opcao != 1 and opcao != 2:
        opcao = int(input('\nOpção inválida! Digite 1 ou 2: '))
    if opcao == 1:
        celsius = float(input('\nQuantos Graus Celsius você gostaria de converter para Fahrenheit? '))
        print(f'\n{celsius:.2f}º C equivale a {(celsius * 1.8) + 32:.2f}º F')
    elif opcao == 2:
        fahrenheit = float(input('\nQuantos Graus Fahrenheit você gostaria de converter para Celsius? '))
        print(f'\n{fahrenheit:.2f}º F equivale a {(fahrenheit - 32) / 1.8:.2f}º C')


