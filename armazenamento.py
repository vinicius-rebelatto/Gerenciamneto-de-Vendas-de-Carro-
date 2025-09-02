from typing import List, Callable
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


def listar_carros(lista_carros: List[dict], criterio: Callable[[dict], bool] = None) -> None: #Essa função chama outra função(topico 8.6) e o mesmo tempo éla é opcional, pois senada for passado ela será deficida como None(Tópico 8.4)
    """
    Lista os carros cadastrados.
    Tópico 8.6: Usa um parâmetro 'criterio' que é uma função.
    Se um critério (função) for fornecido, filtra a lista com base nele.
    Caso contrário, exibe todos os carros.
    """
    print("\n=== Lista de Carros ===")
    if not lista_carros:
        print("Nenhum carro cadastrado ainda.\n")
        return

    # Se um critério foi passado, usa a função para filtrar a lista
    if criterio:
        # Cria uma nova lista apenas com os carros que passam no critério
        carros_a_exibir = [carro for carro in lista_carros if criterio(carro)]
    else:
        # Comportamento padrão: exibe todos
        carros_a_exibir = lista_carros

    if not carros_a_exibir:
        print("Nenhum carro atende ao critério especificado.\n")
        return

    for i, carro in enumerate(carros_a_exibir):
        print(f"[{i}] {carro['modelo']} - {carro['fabricante']} | Preço: R$ {carro['preco']:.2f} | Estoque: {carro['estoque']}")
    print()
