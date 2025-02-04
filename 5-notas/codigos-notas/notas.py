from funcoes_notas import *
texto = 'Calculadora de Notas'
resposta = 'S'
while resposta == 'S':
    try:
        msg(texto)
        notas()
        resposta = input('\nDeseja continuar? (S/N) ').upper()
        while resposta != 'S' and resposta != 'N':
            resposta = input('\nErro: digite S ou N: ').upper()
        print('\n')
    except ValueError:
        print('\nErro: digite um valor numérico.')
print('Obrigado e volte sempre!')
