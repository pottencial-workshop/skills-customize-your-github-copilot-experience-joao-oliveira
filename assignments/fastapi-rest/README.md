# ⚙️ Construindo APIs REST com FastAPI

## 🎯 Objetivo

Aprender a construir APIs REST modernas e documentadas usando o framework FastAPI. O estudante implementará endpoints CRUD, modelagem com Pydantic e verá como a documentação automática (OpenAPI/Swagger) funciona.

## ℹ️ Nível, tempo e pré-requisitos

- Nível: Intermediário
- Tempo estimado: 120–180 minutos
- Pré-requisitos: Python 3.8+, conhecimento básico de HTTP (métodos GET/POST/PUT/DELETE), noções de funções e classes em Python, pip

## 📝 Tarefas

### 🛠️ Task 1 — API CRUD básica (obrigatória)

#### Description
Implemente uma API REST para gerenciar um recurso simples chamado `notes`. Cada nota deve ter um `id` (inteiro), `title` (string) e `content` (string).

#### Requirements
- Implementar endpoints:
  - `GET /notes` — listar todas as notas
  - `POST /notes` — criar uma nova nota
  - `GET /notes/{id}` — recuperar nota por id
  - `PUT /notes/{id}` — atualizar uma nota existente
  - `DELETE /notes/{id}` — excluir uma nota
- Usar Pydantic models para validação de entrada/saída
- Manter os dados em uma estrutura em memória (dicionário/lista) — persistência em arquivo ou banco é opcional
- Retornar códigos HTTP apropriados (200, 201, 404, 400, etc.)
- Documentação automática disponível em `/docs` e `/redoc`

#### Critérios de aceitação
- Endpoints respondem com os status e JSON esperados
- Validação de entrada funciona (ex.: título obrigatório, content não vazio)
- API roda com `uvicorn` sem erros

---

### 🛠️ Task 2 — Documentação e exemplos (importante)

#### Description
Garanta que a API aproveite a documentação automática do FastAPI e forneça exemplos de requests/responses.

#### Requirements
- Exemplos no README de como chamar os endpoints (curl ou HTTPie)
- Confirmar a presença de schemas no Swagger UI (`/docs`)

---

### 🛠️ Task 3 — Desafio (opcional)

- Adicionar paginação em `GET /notes`
- Permitir filtro por palavra-chave no título
- Persistir notas em um arquivo `notes.json` ou SQLite
- Escrever testes simples usando `requests` ou `httpx` e `pytest`

## 🧾 Entregáveis
- `starter-code.py` com a API FastAPI (arquivo principal)
- `requirements.txt` com dependências
- `README.md` preenchido com instruções de execução e exemplos
- (Opcional) `notes.json` ou testes em `tests/`

## ✅ Como testar localmente

1. Instalar dependências:

```bash
python -m pip install -r requirements.txt
```

2. Rodar a API:

```bash
python starter-code.py
```

3. Abrir `http://127.0.0.1:8000/docs` para ver a documentação interativa

## 💡 Dicas
- Separe responsabilidades em funções (ex.: models, operações CRUD, rotas)
- Comece com um repositório em memória; depois adicione persistência se quiser
- Teste pequenos pedaços localmente antes de integrar

<!-- Fim do README da tarefa -->