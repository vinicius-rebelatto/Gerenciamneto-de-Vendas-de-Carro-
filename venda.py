from typing import List
from models import ler_int #8.10 importação de modulos
from constantes import DESCONTO, MIN_VALOR_PARA_DESCONTO # Variaveis Globais 8.1


def vender_carro(lista_carros: List[dict]) -> None:
    print("\n=== Vender Carro ===")
    if len(lista_carros) == 0:
        print("Não há carros cadastrados para vender.\n")
        return

    for i, carro in enumerate(lista_carros):
        print(f"[{i}] {carro['modelo']} - {carro['fabricante']} | R$ {carro['preco']:.2f} | Estoque: {carro['estoque']}")

    indice = ler_int("Escolha o índice do carro: ") # indice -> Var local 8.1
    if indice < 0 or indice >= len(lista_carros):
        print("Índice inválido.\n")
        return

    carro = lista_carros[indice] # carro -> Var local 8.1
    qtd = ler_int("Quantidade desejada: ")
    if qtd <= 0:
        print("Quantidade deve ser maior que zero.\n")
        return

    if qtd > carro['estoque']:
        print("Não há estoque suficiente para essa venda.\n")
        return

    valor_bruto = carro['preco'] * qtd # Var local 8.1
    desconto_aplicado = valor_bruto * DESCONTO if valor_bruto > MIN_VALOR_PARA_DESCONTO else 0.0 # Var local 8.1
    valor_final = valor_bruto - desconto_aplicado # Var local 8.1

    carro['estoque'] -= qtd


    print("\n--- Resumo da Venda ---")
    print(f"Carro: {carro['modelo']} - {carro['fabricante']}")
    print(f"Quantidade: {qtd}")
    print(f"Preço unitário: R$ {carro['preco']:.2f}")
    print(f"Valor bruto: R$ {valor_bruto:.2f}")
    if desconto_aplicado > 0:
        print(f"Desconto ({int(DESCONTO*100)}%): -R$ {desconto_aplicado:.2f}")
    else:
        print("Desconto: R$ 0,00 (não aplicado)")
    print(f"Valor final a pagar: R$ {valor_final:.2f}")
    print(f"Estoque atualizado: {carro['estoque']}\n")