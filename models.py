def criar_carro(modelo, fabricante, preco, estoque):
    if type(modelo) is not str or type(fabricante) is not str:
        raise TypeError("Modelo e fabricante devem ser do tipo string.")
    if type(preco) is not float and type(preco) is not int:
        raise TypeError("Preço deve ser um número inteiro ou de ponto flutuante.")
    if type(estoque) is not int:
        raise TypeError("Estoque deve ser um número inteiro.")

    return {
        "modelo": modelo,
        "fabricante": fabricante,
        "preco": float(preco),
        "estoque": int(estoque),
    }


def ler_str(mensagem: str) -> str:
    valor = input(mensagem).strip()
    while valor == "": # Validação 8.3
        print("Valor não pode ser vazio.")
        valor = input(mensagem).strip()
    return valor


def ler_float(mensagem: str) -> float:
    while True: # Validação 8.3
        texto = input(mensagem).replace(",", ".").strip()
        try:
            return float(texto)
        except ValueError:
            print("Entrada inválida. Digite um número.")


def ler_int(mensagem: str) -> int:
    while True: # Validação 8.3
        texto = input(mensagem).strip()
        try:
            type(texto) # type 8.12
            return int(texto)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")