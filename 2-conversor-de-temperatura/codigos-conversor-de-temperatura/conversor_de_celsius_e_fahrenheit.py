from funcoes_conversor_de_celsius_e_fahrenheit import *
texto = 'Conversor de Temperatura'
msg(texto)
resposta = 'S'
while resposta == 'S':
    try:
        menu()
        resposta = input('\nDeseja continuar? (S/N) ').upper()
        while resposta != 'S' and resposta != 'N':
            resposta = input('\nOpção inválida! Digite S ou N: ').upper()
    except ValueError:
        print('\nOpção inválida! Digite um valor numérico.')
    except TypeError:
        print('\nOpção inválida! Digite um valor numérico.')
print('\nObrigado e volte sempre!')
