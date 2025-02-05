def verifica_senha(senha):
    return '\nSenha válida' if len(senha) >= 8 and any(caracter.isupper() for caracter in senha) and any(digito.isdigit() for digito in senha) else '\nSenha inválida'
