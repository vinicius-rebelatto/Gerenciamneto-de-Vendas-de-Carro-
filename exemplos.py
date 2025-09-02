from models import criar_carro
import random

def fibonacci_recursivo(n: int) -> int:
    """
    Calcula o enésimo termo da sequência de Fibonacci de forma recursiva.
    Exemplo do tópico 8.2, baseado na Listagem 8.14.
    """
    if not isinstance(n, int) or n < 0:
        print("Fibonacci é definido apenas para números inteiros não-negativos.")
        return 0
        
    # Condição de parada: n <= 1 retorna o próprio n (fib(0)=0, fib(1)=1) [cite: 324, 330, 331]
    if n <= 1:
        return n
    # Chamada recursiva: fib(n-1) + fib(n-2) [cite: 324, 333]
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2) #8.2 Funções recursivas

def demonstrar_fibonacci():
    """
    Pede um número ao usuário e exibe o termo correspondente na sequência de Fibonacci.
    """
    print("\n=== Exemplo de Função Recursiva (Fibonacci) ===")
    try:
        num = int(input("Digite a posição desejada na sequência de Fibonacci: "))
        resultado = fibonacci_recursivo(num)
        print(f"O termo na posição {num} da sequência de Fibonacci é {resultado}.\n")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.\n")



def cadastrar_varios_carros(lista_geral_carros: list, *carros_para_cadastrar: list) -> None:
    """
    Cadastra múltiplos carros em uma lista.
    TÓPICO 8.8: Usa '*carros_para_cadastrar' para aceitar um número
    indeterminado de argumentos. Cada argumento é uma lista com os dados de um carro.
    """
    print(f"\nCadastrando {len(carros_para_cadastrar)} novos carros em lote...")
    
    for dados_carro in carros_para_cadastrar:
        # TÓPICO 8.7: Usa o operador '*' para desempacotar a lista 'dados_carro'
        # e passar seus elementos como argumentos para a função criar_carro.
        # Ex: criar_carro(*["Opala", "Chevrolet", 50000, 3]) é o mesmo que
        #     criar_carro("Opala", "Chevrolet", 50000, 3)
        novo_carro = criar_carro(*dados_carro)
        lista_geral_carros.append(novo_carro)
        print(f" -> Carro '{novo_carro['modelo']}' cadastrado.")
    
    print("Cadastro em lote finalizado!\n")


def demonstrar_empacotamento(lista_de_carros: list) -> None:
    """
    Prepara uma lista de dados e chama a função de cadastro em lote.
    """
    # Lista de carros a serem cadastrados. Cada lista interna contém
    # os argumentos na ordem esperada pela função criar_carro.
    carros_novos = [
        ["Opala", "Chevrolet", 50000.00, 3],
        ["Maverick", "Ford", 70000.00, 1],
        ["Brasilia", "VW", 15000.00, 5]
    ]

    # TÓPICO 8.7: Usa o operador '*' para desempacotar a lista 'carros_novos'.
    # Cada lista interna será passada como um argumento separado para a função
    # cadastrar_varios_carros.
    cadastrar_varios_carros(lista_de_carros, *carros_novos)

def demonstrar_sorteio_carro(lista_de_carros: list) -> None:
    """
    Sorteia um carro da lista de carros cadastrados.
    TÓPICO 8.11: Usa a função 'random.sample' para escolher aleatoriamente
    um elemento da lista, simulando um sorteio.
    """
    print("\n=== Sorteio do Carro do Dia! ===")
    if not lista_de_carros:
        print("Não há carros cadastrados para participar do sorteio.\n")
        return

    # random.sample retorna uma nova lista contendo 1 item escolhido aleatoriamente
    carro_sorteado = random.sample(lista_de_carros, 1)[0]
    
    print("🎉 O carro sorteado é... 🎉\n")
    print(f"-> {carro_sorteado['modelo']} - {carro_sorteado['fabricante']}")
    print(f"   Preço: R$ {carro_sorteado['preco']:.2f}\n")
