def criar_carro(modelo, fabricante, preco, estoque): # nomenado paramentro 8.5
    return {
        "modelo": str(modelo),
        "fabricante": str(fabricante),
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