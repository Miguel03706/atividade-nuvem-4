def classificar_numero(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

def main():
    total_pares = 0
    total_impares = 0
    
    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")
        
        if entrada.lower() == "fim":
            break
        
        try:
            numero = int(entrada)
            tipo = classificar_numero(numero)
            
            if tipo == "par":
                total_pares += 1
            else:
                total_impares += 1
            
            print(f"O número {numero} é {tipo}.")
        
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    
    print(f"Total de números pares: {total_pares}")
    print(f"Total de números ímpares: {total_impares}")

main()