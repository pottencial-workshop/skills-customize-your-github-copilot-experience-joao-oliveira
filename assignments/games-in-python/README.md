# 📘 Assignment: Games em Python

## 🎯 Objective

Você irá construir o clássico jogo da forca (Hangman) em Python, praticando manipulação de strings, uso de loops, condicionais e entrada do usuário. O objetivo é desenvolver lógica de programação e interação com o usuário.

## 📝 Tasks

### 🛠️	Jogo da Forca

#### Description
Implemente o jogo da forca, onde o jogador tenta adivinhar uma palavra secreta, letra por letra, antes de esgotar o número de tentativas.

#### Requirements
Completed program should:

- Selecionar aleatoriamente uma palavra de uma lista pré-definida
- Aceitar palpites de letras do usuário e mostrar o progresso atual (ex: `_ _ _ a _`)
- Exibir o número de tentativas incorretas restantes
- Encerrar o jogo quando a palavra for adivinhada ou as tentativas acabarem
- Exibir mensagens de vitória ou derrota ao final

##### Exemplo de entrada/saída:
```
Palavra secreta: _ _ _ _ _
Tentativas restantes: 6
Digite uma letra: a
Progresso: _ a _ _ _
Tentativas restantes: 6
...
Você venceu! A palavra era 'apple'.
```

### 🛠️	Lista de Palavras Personalizada

#### Description
Permita que o usuário insira sua própria lista de palavras para jogar o jogo da forca.

#### Requirements
Completed program should:

- Solicitar ao usuário uma lista de palavras antes de iniciar o jogo
- Utilizar essa lista para selecionar a palavra secreta
- Manter todas as funcionalidades do jogo principal
