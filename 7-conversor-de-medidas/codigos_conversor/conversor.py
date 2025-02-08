from funcoes_conversor import *
resposta = 'S'
while resposta == 'S':
    mensagem = 'Conversor de Medidas'
    print('\n')
    texto(mensagem)
    try:
        opcao = int(input('\nQual a sua opção? '))
        while opcao < 1 or opcao > 8:
            opcao = int(input('\nErro: digite novamente: '))
        if opcao == 1:
            comprimento()
        elif opcao == 2:
            massa()
        elif opcao == 3:
            tempo()
        elif opcao == 4:
            area()
        elif opcao == 5:
            velocidade()
        elif opcao == 6:
            temperatura()
        elif opcao == 7:
            moedas()
        elif opcao == 8:
            liquido()
        resposta = input('\nDeseja continuar? (S/N) ').upper()
        while resposta != 'S' and resposta != 'N':
            resposta = input('\nErro: digite apenas S ou N: ').upper()
    except ValueError:
        print('\nErro: digite novamente!')
print('\nObrigado e volte sempre!')
