import json
import csv
import os

# Carregar estoque do arquivo JSON, se existir
try:
    with open("estoque.json", "r") as arquivo:
        estoque = json.load(arquivo)
except FileNotFoundError:
    estoque = {}

def salvar_estoque():
    with open("estoque.json", "w") as arquivo:
        json.dump(estoque, arquivo)

while True:
    print("\n=== SISTEMA DE ESTOQUE ===")
    print("1. Cadastrar produto")
    print("2. Ver estoque")
    print("3. Entrada de produto")
    print("4. Saída de produto")
    print("5. Gerar relatório")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        try:
            quantidade = int(input("Quantidade inicial: "))
            if quantidade < 0:
                print("Quantidade não pode ser negativa.")
            else:
                estoque[nome] = quantidade
                salvar_estoque()
                print("Produto cadastrado!")
        except ValueError:
            print("Quantidade deve ser um número inteiro.")

    elif opcao == "2":
        print("\nEstoque atual:")
        if not estoque:
            print("Estoque vazio.")
        else:
            for produto, quantidade in estoque.items():
                status = "⚠ ESTOQUE BAIXO" if quantidade <= 5 else ""
                print(f"{produto}: {quantidade} {status}")

    elif opcao == "3":
        nome = input("Nome do produto: ")
        if nome in estoque:
            try:
                quantidade = int(input("Quantidade de entrada: "))
                if quantidade < 0:
                    print("Quantidade não pode ser negativa.")
                else:
                    estoque[nome] += quantidade
                    salvar_estoque()
                    print("Entrada registrada!")
            except ValueError:
                print("Quantidade deve ser um número inteiro.")
        else:
            print("Produto não encontrado.")

    elif opcao == "4":
        nome = input("Nome do produto: ")
        if nome in estoque:
            try:
                quantidade = int(input("Quantidade vendida: "))
                if quantidade < 0:
                    print("Quantidade não pode ser negativa.")
                elif estoque[nome] >= quantidade:
                    estoque[nome] -= quantidade
                    salvar_estoque()
                    print("Saída registrada!")
                else:
                    print("Estoque insuficiente.")
            except ValueError:
                print("Quantidade deve ser um número inteiro.")
        else:
            print("Produto não encontrado.")

    elif opcao == "5":
        with open("relatorio_estoque.csv", "w", newline="") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["Produto", "Quantidade"])
            for produto, quantidade in estoque.items():
                writer.writerow([produto, quantidade])
        print("Relatório gerado e aberto no Excel!")
        os.startfile("relatorio_estoque.csv")

    elif opcao == "6":
        salvar_estoque()
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")