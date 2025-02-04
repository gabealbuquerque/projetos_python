def notas():
    nome = input('\nDigite o nome do aluno: ')
    while nome == '' :
        nome = input('\nErro: digite um nome: ')
    nota1 = float(input('\nDigite a 1ª nota: '))
    while nota1 > 10 or nota1 < 0:
        nota1 = float(input('\nErro: não é possível uma nota ter esse valor. Digite novamente: '))
    nota2 = float(input('\nDigite a 2ª nota: '))
    while nota2 > 10 or nota2 < 0:
        nota2 = float(input('\nErro: não é possível uma nota ter esse valor. Digite novamente: '))
    nota3 = float(input('\nDigite a 3ª nota: '))
    while nota3 > 10 or nota3 < 0:
        nota3 = float(input('\nErro: não é possível uma nota ter esse valor. Digite novamente: '))
    media = ((nota1 + nota2 + nota3) / 3)
    media_nota(nome, media)

def media_nota(nome, media):
    if media >= 6:
        print(f'\nO aluno {nome} foi aprovado com média final: {media:.2f}!')
    else:
        pontos = 6 - media
        print(f'\nO aluno {nome} foi reprovado com média final: {media:.2f} e precisou de {pontos:.2f} para passar.')

def msg(texto):
    print('-_' * len(texto))
    print('{:^40}'.format(texto))
    print('-_' * len(texto))
