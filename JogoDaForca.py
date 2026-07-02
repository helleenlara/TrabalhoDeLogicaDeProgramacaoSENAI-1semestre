# ============================================
# SENAI BAHIA - Dendezeiros
# Curso: Técnico em Desenvolvimento de Sistemas
# Disciplina: Lógica de Programação
# Docente: Lucas Almeida
# Turma: 103513 | Data: 06/07/2026
# Grupo: Ana Beatriz Bispo, Lara Hellen Marques,
#        Micaela Oliveira, Rafaela Lembrança
# ============================================


# Importa o módulo de sorteio do Python
import random

# Dicionário com categorias de palavras
# Cada categoria tem sua própria lista de palavras
categorias = {
    "1": {
        "nome": "Tecnologia",
        "palavras": [
            "python", "computador", "teclado", "monitor", "internet",
            "programa", "variavel", "funcao", "lista", "loop",
            "codigo", "terminal", "arquivo", "sistema", "software"
        ]
    },
    "2": {
        "nome": "Escola",
        "palavras": [
            "caderno", "caneta", "mochila", "professor", "disciplina",
            "turma", "prova", "nota", "aula", "intervalo",
            "biblioteca", "quadro", "borracha", "lapis", "apostila"
        ]
    },
    "3": {
        "nome": "Animais",
        "palavras": [
            "cachorro", "gato", "papagaio", "tartaruga", "hamster",
            "coelho", "peixe", "cobra", "lagarto", "passaro",
            "elefante", "girafa", "macaco", "pinguim", "golfinho"
        ]
    }
}


# Desenhos da forca — cada index é um estado do boneco
# index 0 = nenhum erro, index 6 = boneco completo (perdeu)
forca = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
==========""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
==========""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
==========""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
==========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
==========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
==========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========="""]


# Função que exibe o desenho da forca de acordo com os erros cometidos
def exibir_forca(erros):
    print(forca[erros])


# Função que coloca a letra no lugar certo do progresso quando o jogador acerta
def atualizar_progresso(palavra, letra, progresso):
    for i in range(len(palavra)):
        if palavra[i] == letra:
            progresso[i] = letra


# Função que exibe o estado atual do jogo a cada rodada
def exibir_jogo(progresso, letras_usadas, tentativas_restantes):
    # Calcula quantos erros foram cometidos para mostrar o desenho certo
    erros = 6 - tentativas_restantes
    exibir_forca(erros)
    print("Palavra: " + " ".join(progresso))
    print("Tentativas restantes:", tentativas_restantes)
    if letras_usadas:
        print("Letras usadas:", ", ".join(sorted(letras_usadas)))
    print("=" * 40)


# Função que mostra o menu de categorias e retorna a escolhida pelo jogador
def escolher_categoria():
    print("\nEscolha uma categoria:")
    print("1 - Tecnologia")
    print("2 - Escola")
    print("3 - Animais")

    # Fica pedindo até o jogador digitar uma opção válida
    while True:
        escolha = input("\nDigite o número da categoria: ")
        if escolha in categorias:
            return categorias[escolha]
        print("Opção inválida! Digite 1, 2 ou 3.")


# Função principal que roda uma partida completa do jogo
def jogar():
    # Mensagem de boas-vindas exibida no início de cada partida
    print("\n" + "=" * 40)
    print("    Bem-vindas ao Jogo da Forca!")
    print("=" * 40)

    # Jogador escolhe a categoria
    categoria = escolher_categoria()

    # Sorteia uma palavra aleatória da categoria escolhida
    palavra_secreta = random.choice(categoria["palavras"])

    # Cria o progresso com um _ para cada letra da palavra sorteada
    progresso = ["_"] * len(palavra_secreta)

    # Lista de letras usadas, começa vazia
    letras_usadas = []

    # Avisa a categoria e quantas letras tem a palavra
    print(f"\nCategoria: {categoria['nome']}")
    print(f"A palavra tem {len(palavra_secreta)} letras. Boa sorte!\n")

    # Número máximo de erros permitidos
    max_tentativas = 6
    tentativas_restantes = max_tentativas

    # Loop principal — roda enquanto ainda há tentativas e letras ocultas
    while tentativas_restantes > 0 and "_" in progresso:

        # Exibe o estado atual do jogo
        exibir_jogo(progresso, letras_usadas, tentativas_restantes)

        # Pede que o jogador digite uma letra
        letra = input("Digite uma letra: ").lower()

        # Validação 1: verifica se digitou exatamente uma letra válida
        if len(letra) != 1 or not letra.isalpha():
            print("Digite apenas uma letra!")

        # Validação 2: verifica se a letra já foi tentada antes
        elif letra in letras_usadas:
            print("Você já usou essa letra! Tente outra.")

        # Letra válida e nova: processa normalmente
        else:
            letras_usadas.append(letra)
            if letra in palavra_secreta:
                print("Boa! Essa letra está na palavra!")
                atualizar_progresso(palavra_secreta, letra, progresso)
            else:
                print("Essa letra não está na palavra.")
                tentativas_restantes -= 1

    # Exibe o estado final antes de mostrar o resultado
    exibir_jogo(progresso, letras_usadas, tentativas_restantes)

    # Verifica o resultado depois que o loop encerrar
    if "_" not in progresso:
        print("Parabéns! Você ganhou! 🎉")
    else:
        print("Você perdeu. A palavra era:", palavra_secreta.upper())

    # Pergunta se quer jogar de novo e reinicia o jogo se quiser
    jogar_de_novo = input("\nQuer jogar de novo? (s/n): ").lower()
    if jogar_de_novo == "s":
        jogar()
    else:
        print("\nObrigada por jogar! Até a próxima. 👋")


# Inicia o jogo
jogar()