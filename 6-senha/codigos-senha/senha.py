from funcoes_senha import *
while True:
    senha = input('\nDigite uma senha: ')
    resultado = verifica_senha(senha)
    print(resultado)
    if resultado == '\nSenha válida':
        break
