# Este é o conversor-de-dolar-e-euro nº 2 (mais completo).
# Há também o conversor nº 1, sendo mais simples
from funcoes_conversor_de_dolar_e_euro_2 import *
texto = 'Conversor de Moedas'
msg(texto)
print('''\nCotação do dólar: R$ 1.00 = US$ 5.85
Cotação do euro: R$ 1.00 = EUR 6.40''')
resposta = 'S'
while resposta == 'S':
    try:
        print('''\nEscolha uma das opções abaixo\n
    1: Real - Dólar
    2: Dólar - Real
    3: Real - Euro
    4: Euro - Real\n''')
        menu()
        resposta = input('\nDeseja continuar? (S/N) ').upper()
        while resposta != 'S' and resposta != 'N':
            resposta = input('\nOpção inválida! Digite S ou N: ').upper()
    except ValueError:
        print('\nOpção inválida! Digite um valor numérico.')
    except TypeError:
        print('\nOpção inválida! Digite um valor numérico.')
print('\nVolte sempre!')
