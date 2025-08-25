def criar_carro(modelo, fabricante, preco, estoque):
    return {
        "modelo": str(modelo),
        "fabricante": str(fabricante),
        "preco": float(preco),
        "estoque": int(estoque),
    }


def ler_str(mensagem: str) -> str:
    valor = input(mensagem).strip()
    while valor == "":
        print("Valor não pode ser vazio.")
        valor = input(mensagem).strip()
    return valor


def ler_float(mensagem: str) -> float:
    while True:
        texto = input(mensagem).replace(",", ".").strip()
        try:
            return float(texto)
        except ValueError:
            print("Entrada inválida. Digite um número.")


def ler_int(mensagem: str) -> int:
    while True:
        texto = input(mensagem).strip()
        try:
            return int(texto)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")