def msg(texto):
    print('-_' * len(texto))
    print('{:^25}'.format(texto))
    print('-_' * len(texto))

def tabuada():
    resposta = 'S'
    while resposta == 'S':
        try:
            num = int(input('\nDigite um número para ver sua tabuada: '))
            while num == 0:
                num = int(input('\nErro: não há tabuada do zero. Digite um outro número: '))
            limite = int(input('\nDigite até que número você gostaria de ver a tabuada: '))
            print('\n')
            i = 0
            while i <= limite:
                print(f'{num} x {i} = {num * i}')
                i += 1
            resposta = input('\nGostaria de continuar? (S/N) ').upper()
            while resposta != 'S' and resposta != 'N':
                resposta = input('\nErro: digite S ou N: ').upper()
        except ValueError:
            print('\nErro: digite um número inteiro.')
