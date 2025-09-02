from typing import List
from armazenamento import cadastrar_carro, listar_carros
from venda import vender_carro
from exemplos import demonstrar_fibonacci, demonstrar_empacotamento, demonstrar_sorteio_carro
from criterios import estoque_baixo, eh_caro


def mostrar_menu():
    print("==========================")
    print("   LOJA DE CARROS - Menu  ")
    print("==========================")
    print("1 - Cadastrar carro")
    print("2 - Listar carros")
    print("3 - Vender carro")
    print("4 - Exemplo Recursão (Fibonacci)")
    print("5 - Cadastrar em Lote (Ex. 8.7/8.8)")
    print("6 - Sorteio de Carro (Ex. 8.11)")
    print("0 - Sair")


def main():
    carros: List[dict] = []
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_carro(carros)
        elif opcao == "2":
            # --- LÓGICA PARA PASSAR FUNÇÕES COMO PARÂMETRO ---
            print("\n--- Opções de Listagem ---")
            print("1 - Listar todos os carros")
            print("2 - Listar carros com estoque baixo (< 5 unidades)")
            print("3 - Listar carros caros (> R$ 150.000)")
            print("4 - Listar carros da VW (Exemplo Lambda)") # <-- 1. ADICIONE A NOVA OPÇÃO
            sub_opcao = input("Escolha como deseja listar: ").strip()

            if sub_opcao == '1':
                listar_carros(carros)
            elif sub_opcao == '2':
                listar_carros(carros, criterio=estoque_baixo)
            elif sub_opcao == '3':
                listar_carros(carros, criterio=eh_caro)
            elif sub_opcao == '4':
                # TÓPICO 8.9: Em vez de definir uma função com 'def',
                # criamos uma função anônima na hora com 'lambda'.
                # A linha abaixo cria uma função que recebe 'carro' e retorna
                # True se o fabricante for 'vw', e False caso contrário.
                listar_carros(carros, criterio=lambda carro: carro['fabricante'].lower() == 'vw') #Uso da função lambda
            else:
                print("Opção de listagem inválida.\n")
            # --- FIM DA LÓGICA ---
        
        # ... (o resto do laço 'while' continua como está no seu arquivo)
        elif opcao == "3":
            vender_carro(carros)
        elif opcao == "4":
            demonstrar_fibonacci()
        elif opcao == "5":
             demonstrar_empacotamento(carros)
        elif opcao == "6":
            demonstrar_sorteio_carro(carros)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()