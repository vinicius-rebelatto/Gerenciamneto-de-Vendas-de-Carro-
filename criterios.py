def estoque_baixo(carro: dict) -> bool:
    """Retorna True se o estoque do carro for menor que 5."""
    return carro['estoque'] < 5

def eh_caro(carro: dict) -> bool:
    """Retorna True se o preço do carro for maior que R$ 150.000."""
    return carro['preco'] > 150000.00