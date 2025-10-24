# 🎮 Games em Python

## 🎯 Objetivo

Desenvolver o jogo da forca (Hangman) em Python para praticar manipulação de strings, loops, condicionais e interação com o usuário. Conteúdo focado em aprendizado com linguagem clara e encorajadora.

## ℹ️ Nível, tempo e pré-requisitos

- Nível: Iniciante / Intermediário
- Tempo estimado: 60–120 minutos
- Pré-requisitos: Noções básicas de Python (variáveis, listas, loops, condicionais, entrada/saída)

## 📝 Tarefas

### 🛠️ Task 1 — Implementar Jogo da Forca

#### Description
Implemente um programa em Python que permita ao jogador adivinhar uma palavra secreta, letra por letra, antes de esgotar o número de tentativas.

#### Requirements
O programa deve:

- Selecionar aleatoriamente uma palavra de uma lista pré-definida
- Aceitar palpites de letras do usuário e mostrar o progresso atual (ex.: `_ _ _ a _`)
- Exibir o número de tentativas incorretas restantes
- Encerrar o jogo quando a palavra for adivinhada ou as tentativas acabarem
- Exibir mensagem de vitória ou derrota ao final

#### Exemplo de entrada/saída
```
Palavra secreta: _ _ _ _ _
Tentativas restantes: 6
Digite uma letra: a
Progresso: _ a _ _ _
Tentativas restantes: 6
...
Você venceu! A palavra era 'apple'.
```

#### Critérios de aceitação
- Código rodando em Python 3 sem erros
- Interface de texto clara com progresso e tentativas visíveis
- Tratamento básico de entradas inválidas (ex.: múltiplas letras, caracteres não alfabéticos)

---

### 🛠️ Task 2 — Lista de Palavras Personalizada (Desafio)

#### Description
Permita que o usuário forneça sua própria lista de palavras antes de iniciar o jogo.

#### Requirements
O programa estendido deve:

- Solicitar ao usuário uma lista de palavras (ou carregar de um arquivo) antes de começar
- Usar essa lista para escolher a palavra secreta de forma aleatória
- Manter todas as funcionalidades do jogo principal

#### Sugestões de implementação
- Separar responsabilidades em funções (ex.: selecionar_palavra, exibir_progresso, processar_palpite)
- Permitir opção padrão (lista interna) caso o usuário não queira inserir palavras
- Validar entradas da lista (palavras não vazias, sem espaços)

---

## 🧾 Entregáveis
- Arquivo principal (ex.: hangman.py) com código comentado
- (Opcional) arquivo de palavras (words.txt) se optar por carregar de arquivo
- Instruções rápidas na primeira execução descrevendo como jogar

## 💡 Dicas finais
- Comece implementando a lógica de atualização do progresso para cada letra
- Teste com palavras curtas e longas
- Mantenha mensagens amigáveis para o estudante

<!-- Fim do arquivo -->
