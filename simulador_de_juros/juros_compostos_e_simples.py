from sre_constants import error

from funcoes_simulador import *
# Simulador de investimento que retorna o montante final e o juros simples e composto
print('-' * 25, 'Simulador de Investimento', '-' * 25)
continua = 'S'
try:
    while continua == 'S':
        resposta = menu()
        if resposta == 1:
            Capital = capital()
            Juros = juros()
            Tempo = tempo()
            juros_simples(Capital, Juros, Tempo)
        elif resposta == 2:
            Capital = capital()
            Juros = juros()
            Tempo = tempo()
            juros_composto(Capital, Juros, Tempo)
        else:
            resposta = int(input('\033[1:31mErro: opção inválida!\033[m Digite 1 ou 2: '))
        continua = input('Deseja realizar outra simulação? (S/N) ').upper()
    while continua not in 'SN':
            continua = input('\033[1:31mErro: opção inválida.\033[m Digite S ou N: ').upper()
except ValueError:
    print('Opção inválida! \033[1:31mValor inválido.\033[m')
except TypeError:
    print('Opção inválida! \033[1:31mTipo inválido.\033[m')
finally:
    print('Obrigado e volte sempre!')

