from typing import List
from models import criar_carro, ler_str, ler_float, ler_int


def cadastrar_carro(lista_carros: List[dict]) -> None:
    print("\n=== Cadastro de Carro ===")
    modelo = ler_str("Modelo do carro: ")
    fabricante = ler_str("Fabricante: ")
    preco = ler_float("Preço (R$): ")
    estoque = ler_int("Quantidade em estoque: ")

    carro = criar_carro(modelo, fabricante, preco, estoque)
    lista_carros.append(carro)
    print("Carro cadastrado com sucesso!\n")


def listar_carros(lista_carros: List[dict]) -> None:
    print("\n=== Lista de Carros ===")
    if len(lista_carros) == 0:
        print("Nenhum carro cadastrado ainda.\n")
        return

    for i, carro in enumerate(lista_carros):
        print(f"[{i}] {carro['modelo']} - {carro['fabricante']} | Preço: R$ {carro['preco']:.2f} | Estoque: {carro['estoque']}")
    print()