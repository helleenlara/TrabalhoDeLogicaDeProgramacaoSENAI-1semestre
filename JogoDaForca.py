# ============================================
# Jogo da Forca
# Disciplina: Lógica de Programação
# Grupo: [Nome 1], [Nome 2], [Nome 3], [Nome 4]
# Turma: [turma] | Data: [data de entrega]
# ============================================


# ============================================
# PESSOA 1 — Lista de palavras e sorteio
# ============================================

# Importa o módulo de sorteio do Python
import random

# Cria a lista com todas as palavras possíveis do jogo
palavras = ['borboleta', 'chocolate', 'computador', 'cachorro', 'floresta', 'montanha', 'guitarra', 'celular', 'planeta', 'futebol', 'cozinha', 'viagem', 'oceano', 'monitor', 'diamante']

# Sorteia uma palavra aleatória da lista e guarda em palavra_secreta

sorteio = random.choice(palavras)

print(sorteio)

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

# Define o número máximo de tentativas (erros permitidos = 6)

# Cria a variável que vai diminuindo conforme o jogador erra



# ============================================
# PESSOA 2 — Loop principal do jogo
# ============================================

# Inicia o loop que mantém o jogo rodando
# Condição: ainda tem tentativas E ainda tem _ no progresso
# (quando qualquer uma dessas condições for falsa, o loop para)

    # ---- PESSOA 4 ----
    # Chama a função que exibe o estado atual do jogo

    # ---- PESSOA 2 ----
    # Pede que o jogador digite uma letra
    # (use .lower() para converter para minúsculo)

    # ---- PESSOA 3 — Validação 1: entrada inválida ----
    # Verifica se o jogador digitou exatamente uma letra
    # (usa len() para checar o tamanho e .isalpha() para checar se é letra)
    # Se inválido: avisa e volta para o início do loop (continue)

    # ---- PESSOA 3 — Validação 2: letra já usada ----
    # Verifica se a letra digitada já está na lista letras_usadas
    # Se sim: avisa e volta para o início do loop (continue)

    # ---- PESSOA 3 — Processamento: letra válida e nova ----
    # Adiciona a letra na lista de letras_usadas

        # ---- PESSOA 3 ----
        # Se a letra estiver na palavra_secreta:
        # mostra mensagem de acerto e chama atualizar_progresso()

        # ---- PESSOA 2 ----
        # Se a letra NÃO estiver na palavra_secreta:
        # mostra mensagem de erro e diminui tentativas_restantes em 1


# ============================================
# PESSOA 2 — Resultado final do jogo
# ============================================

# Depois que o loop terminar, verifica o resultado:

    # Se não tiver mais _ no progresso: o jogador ganhou
    # Mostra mensagem de parabéns

    # Se ainda tiver _: o jogador perdeu (tentativas acabaram)
    # Mostra mensagem de derrota e revela a palavra_secreta


# ============================================
# PESSOA 4 — Jogar de novo
# ============================================

# Pergunta se o jogador quer jogar de novo (s/n)

    # Se a resposta for "s":
    # (o grupo combina aqui como vai reiniciar o jogo)

    # Se a resposta for "n":
    # Mostra uma mensagem de despedida