from funcoes_simulador import *
# Simulador de investimento que retorna o montante final e o juros simples e composto
print('-' * 25, 'Simulador de Investimento', '-' * 25)
continua = 'S'
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
    continua = input('Deseja realizar outra simulação? (S/N) ').upper()
while continua not in 'SN':
        continua = input('Erro: opção inválida. Digite S ou N: ').upper()
print('Obrigado e volte sempre!')
