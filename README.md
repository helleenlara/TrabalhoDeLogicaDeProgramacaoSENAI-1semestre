# Jogo da Forca

**Instituição:** SENAI BAHIA — Dendezeiros  
**Curso:** Técnico em Desenvolvimento de Sistemas  
**Disciplina:** Lógica de Programação  
**Docente:** Lucas Almeida  
**Turma:** 103513 | **Data:** 06/07/2026  
**Grupo:** Ana Beatriz Bispo, Lara Hellen Marques, Micaela Oliveira, Rafaela Lembrança  

---

## Objetivo

Desenvolver um jogo da forca funcional em Python como projeto prático da disciplina de Lógica de Programação, aplicando os conceitos estudados no primeiro semestre: variáveis, listas, condições, loops e funções.

---

## O que o jogo faz

- Sorteia uma palavra aleatória de uma lista criada pelo grupo
- Mostra a palavra com underlines no lugar das letras ocultas
- Permite que o jogador adivinhe uma letra por vez
- Avisa se a letra já foi tentada antes
- Controla o número de tentativas — o jogador tem até 6 erros
- Ao final, informa se o jogador ganhou ou perdeu e revela a palavra

---

## Como executar

1. Ter o Python instalado no computador (versão 3 ou superior)
2. Baixar o arquivo `forca.py`
3. Abrir o terminal na pasta onde o arquivo está
4. Executar o comando:

```
python forca.py
```

---

## Como jogar

1. O programa sorteia uma palavra e mostra quantas letras ela tem
2. Digite uma letra e pressione Enter
3. Se a letra estiver na palavra, ela aparece no lugar certo
4. Se não estiver, você perde uma tentativa
5. Você tem 6 tentativas erradas antes de perder
6. Adivinhe todas as letras antes de acabar as tentativas para ganhar

---

## Tecnologias usadas

- **Python 3** — linguagem principal
- **Módulo random** — usado para sortear a palavra (já vem instalado com o Python, sem necessidade de instalar nada extra)
