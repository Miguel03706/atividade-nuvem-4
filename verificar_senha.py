def verificar_senha(senha):
    if len(senha) < 8:
        return "Senha fraca: deve ter pelo menos 8 caracteres."
    
    if not any(char.isdigit() for char in senha):
        return "Senha fraca: deve conter pelo menos um número."
    
    return "Senha forte!"

def main():
    while True:
        senha = input("Digite a senha (ou 'sair' para encerrar): ")
        
        if senha.lower() == "sair":
            print("Programa encerrado.")
            break
        
        resultado = verificar_senha(senha)
        print(resultado)
        
        if resultado == "Senha forte!":
            break

main()