from math import pow
from funcoes_simulador import *
# Simulador de investimento que retorna o montante final e o juros simples e composto
print('-' * 25, 'Simulador de Investimento', '-' * 25)
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
