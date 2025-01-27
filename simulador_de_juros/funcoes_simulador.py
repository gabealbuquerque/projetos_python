from math import pow
def juros_composto(capital, juros, tempo):
    'retorna o valor final de investimento (já incluído o juros)'
    montante_composto = capital*pow((1+juros), tempo)
    print(f'O montante composto foi de: R$ {montante_composto:.2f}')
    print(f'O juros foi de: R$ {montante_composto - capital:.2f}')

def juros_simples(capital, juros, tempo):
    'retorna apenas o valor de juros (sendo somado no prog principal ao capital)'
    montante_simples = capital * juros * tempo
    print(f'O montante simples foi de: R$ {montante_simples + capital:.2f}')

def capital():
    return float(input('Digite o capital: R$ '))

def juros():
    return float(input('Digite o juros anual em porcentagem (%): ')) / 100

def tempo():
    return int(input('Digite quantos meses será o investimento: ')) / 12

def menu():
    return int(input('''Escolha uma das opções abaixo:
    1 - Juros Simples
    2 - Juros Composto
    Qual opção você escolhe? '''))