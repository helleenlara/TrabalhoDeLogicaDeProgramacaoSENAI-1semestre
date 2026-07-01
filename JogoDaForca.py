# SENAI BAHIA - Dendezeiros
# Curso: Técnico em Desenvolvimento de Sistemas
# Disciplina: Lógica de Programação
# Docente: Lucas Almeida
# Turma: 103513 | Data: 06/07/2026
# Grupo: Ana Beatriz Bispo, Lara Hellen Marques, Micaela Oliveira , Rafaela Lembrança


# ----------JOGO DA FORCA----------

import random

palavras = ['borboleta', 'chocolate', 'computador', 'cachorro', 'floresta', 'montanha', 'guitarra', 'celular', 'planeta', 'futebol', 'cozinha', 'viagem', 'oceano', 'monitor', 'diamante']

palavra_secreta = random.choice(palavras)

# ============================================
# PESSOA 4 — Exibição: criação do progresso e das listas
# ============================================

# Cria a lista de progresso com um _ para cada letra da palavra_secreta
# Ex: se a palavra tem 4 letras → ['_', '_', '_', '_']


# Cria a lista de letras usadas, começa vazia
# (vai guardar todas as letras que o jogador já tentou)



# ============================================
# PESSOA 4 — Função: atualizar o progresso
# ============================================

# Define a função que coloca a letra no lugar certo do progresso
# quando o jogador acerta
# Recebe: a palavra secreta, a letra acertada e a lista de progresso
# Não retorna nada — ela altera a lista diretamente

    # Percorre cada posição da palavra
        # Se a letra nessa posição for igual à letra acertada,
        # substitui o _ pelo letra no progresso



# ============================================
# PESSOA 4 — Função: exibir o estado do jogo
# ============================================

# Define a função que mostra tudo que o jogador precisa ver
# a cada rodada: a palavra com os _ e letras descobertas,
# as letras erradas já tentadas e as tentativas restantes
# Recebe: progresso, letras_usadas, tentativas_restantes

    # Mostra uma linha separadora para organizar visualmente

    # Mostra a palavra com as letras descobertas e _ nos lugares ocultos
    # (use " ".join(progresso) para separar os caracteres com espaço)

    # Mostra quantas tentativas ainda restam

    # Se já houver letras usadas, mostra a lista em ordem alfabética

    # Fecha com outra linha separadora



# ============================================
# PESSOA 4 — Mensagem de boas-vindas
# ============================================

# Mostra o título do jogo e uma mensagem de boas-vindas para o jogador
# (essa parte roda uma vez só, antes do loop começar)



# ============================================
# PESSOA 2 — Configuração do loop
# ============================================

max_tentativas = 6
tentativas_restantes = max_tentativas

while tentativas_restantes > 0 and "_" in progresso:

    exibir_jogo(progresso, letras_usadas, tentativas_restantes)

    letra = input("Digite uma letra: ").lower()

    # ---- PESSOA 3 ----
    # Chama a função que exibe o estado atual do jogo

    if len(letra) != 1 or not letra.isalpha():
        print("Digite apenas uma letra!")

    elif letra in letras_usadas:
        print("Você já usou essa letra! Tente outra.")

    else:
        letras_usadas.append(letra)
        if letra in palavra_secreta:
            print("Boa! Essa letra está na palavra!")
            atualizar_progresso(palavra_secreta, letra, progresso)  # Pessoa 4
        else:
            print("Essa letra não está na palavra.")
            tentativas_restantes -= 1

# ---- PESSOA 2 ----           
 
if "_" not in progresso:
    print("Parabéns! Você ganhou! 🎉")
else:
    print(f"Você perdeu. A palavra era: {palavra_secreta}")

# ============================================
# PESSOA 4 — Jogar de novo
# ============================================

# Pergunta se o jogador quer jogar de novo (s/n)

    # Se a resposta for "s":
    # (o grupo combina aqui como vai reiniciar o jogo)

    # Se a resposta for "n":
    # Mostra uma mensagem de despedida