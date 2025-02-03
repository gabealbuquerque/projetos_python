def msg(texto):
    print('-_' * len(texto))
    print('{:^22}'.format(texto))
    print('-_' * len(texto))

def calculadora():
    resposta = 'S'
    while resposta == 'S':
        try:
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
            resposta = input('\nDeseja continuar? (S/N) ').upper()
            while resposta != 'S' and resposta != 'N':
                resposta = input('\nErro: digite S ou N: ').upper()
        except ValueError:
            print('\nErro: digite um valor numérico.')
        except ZeroDivisionError:
            print('\nErro: não é possível fazer divisão por zero.')
