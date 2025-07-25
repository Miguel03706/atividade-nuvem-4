def registrar_notas():
    notas = []
    
    while True:
        entrada = input("Digite uma nota entre 0 e 10 ou 'fim' para encerrar: ")
        
        if entrada.lower() == 'fim':
            break
        
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Deve ser entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número real ou 'fim'.")
    
    if notas:
        media = sum(notas) / len(notas)
        print(f"Média da turma: {media:.2f}")
        print(f"Total de notas válidas registradas: {len(notas)}")
    else:
        print("Nenhuma nota válida foi registrada.")

registrar_notas()