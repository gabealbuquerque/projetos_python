from funcoes_conversor import *
resposta = 'S'
while resposta == 'S':
    mensagem = 'Conversor de Medidas'
    print('\n')
    texto(mensagem)
    try:
        opcao = int(input('\nQual a sua opção? '))
        while opcao < 1 or opcao > 5:
            opcao = int(input('\nErro: digite novamente: '))
        if opcao == 1:
            menu1()
            menu_1 = int(input('\nQual a sua opção? '))
            while menu_1 < 1 or menu_1 > 4:
                menu_1 = int(input('\nErro: digite uma opção válida: '))
            if menu_1 == 1:
                comprimento()
            elif menu_1 == 2:
                tempo()
            elif menu_1 == 3:
                velocidade()
            elif menu_1 == 4:
                area()
        elif opcao == 2:
            menu2()
            menu_2 = int(input('\nQual a sua opção? '))
            while menu_2 < 1 or menu_2 > 2:
                menu_2 = int(input('\nErro: digite uma opção válida: '))
            if menu_2 == 1:
                massa()
            elif menu_2 == 2:
                imc()
        elif opcao == 3:
            menu3()
            menu_3 = int(input('\nQual a sua opção? '))
            while menu_3 < 1 or menu_3 > 2:
                menu_3 = int(input('\nErro: digite uma opção válida: '))
            if menu_3 == 1:
                temperatura()
            elif menu_3 == 2:
                liquido()
        elif opcao == 4:
            menu4()
            menu_4 = int(input('\nQual a sua opção? '))
            while menu_4 < 1 or menu_4 > 2:
                menu_4 = int(input('\nErro: digite uma opção válida: '))
            if menu_4 == 1:
                moedas()
            elif menu_4 == 2:
                calculadora()
        elif opcao == 5:
            menu5()
            menu_5 = int(input('\nQual a sua opção? '))
            while menu_5 < 1 or menu_5 > 2:
                menu_5 = int(input('\nErro: digite uma opção válida: '))
            if menu_5 == 1:
                notas()
            elif menu_5 == 2:
                tabuada()
        resposta = input('\nDeseja continuar? (S/N) ').upper()
        while resposta != 'S' and resposta != 'N':
            resposta = input('\nErro: digite apenas S ou N: ').upper()
    except ValueError:
        print('\nErro: digite novamente!')
print('\nObrigado e volte sempre!')
