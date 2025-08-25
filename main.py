from typing import List
from armazenamento import cadastrar_carro, listar_carros
from venda import vender_carro


def mostrar_menu():
    print("==========================")
    print("   LOJA DE CARROS - Menu  ")
    print("==========================")
    print("1 - Cadastrar carro")
    print("2 - Listar carros")
    print("3 - Vender carro")
    print("0 - Sair")


def main():
    carros: List[dict] = []
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_carro(carros)
        elif opcao == "2":
            listar_carros(carros)
        elif opcao == "3":
            vender_carro(carros)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()