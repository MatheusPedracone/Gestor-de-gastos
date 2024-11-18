def calcular_despesas():
    renda = float(input("Digite sua renda mensal: "))
    despesas = []
    while True:
        descricao = input("Descrição da despesa (ou 'sair' para terminar): ")
        if descricao.lower() == 'sair':
            break
        valor = float(input(f"Valor da despesa '{descricao}': "))
        despesas.append(valor)
    
    total_despesas = sum(despesas)
    saldo = renda - total_despesas
    
    print(f"\nTotal de despesas: R${total_despesas:.2f}")
    print(f"Saldo restante: R${saldo:.2f}")

calcular_despesas()

