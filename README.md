# My Agenda API (FastAPI + SQLAlchemy + Alembic)

API para gerenciamento da aplicação my-agenda-app
Link do repositório frontend: https://github.com/AnaLinsDev/my-agenda-app
---

## 📦 Requisitos

- Python 3.10+
- pip
- Docker (recomendado) → :contentReference[oaicite:0]{index=0}
- (Opcional) PostgreSQL → :contentReference[oaicite:1]{index=1}

---

## 🚀 Setup do projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/AnaLinsDev/my-agenda-api.git
cd my-agenda-api
```

---

## 3. Insira as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL="postgresql://postgres:postgres@localhost:5432/agenda_local"
RUN_MIGRATIONS="false" # false (venv) ou true (docker)
NODE_ENV="dev"
JWT_SECRET="my_jwt_secret_key"
JWT_EXPIRES_IN="7d"
ALGORITHM = "HS256"
```

---

## Rodar a aplicação usando Venv

### 1. Criar ambiente virtual (venv)

```bash
python -m venv venv
```

Ativar:

* Windows (CMD):

```bash
venv\Scripts\activate
```

* Windows (PowerShell):

```bash
venv\Scripts\Activate.ps1
```

* Linux / macOS:

```bash
source venv/bin/activate
```

---

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Rodar a aplicação

```bash
uvicorn app.main:app --reload
```

---

## Rodar a aplicação usando Docker

### 1. Build e subir containers

```bash
docker compose up --build
```

### 2. Parar containers

```bash
docker compose down
```


### 3. Resetar banco (apagar dados)

```bash
docker compose down -v
```



A API estará disponível em:

* http://localhost:8000
* Docs: http://localhost:8000/docs


---

## Banco de dados e migrations (Alembic)

### Criar uma nova migration

Sempre que alterar os models:

```bash
alembic revision --autogenerate -m "description of changes"
```

---

### Revisar a migration

Antes de aplicar, abra o arquivo gerado em:

```bash
alembic/versions/
```

Verifique:

* tabelas criadas corretamente
* foreign keys
* tipos de dados

---

### Aplicar migration

```bash
alembic upgrade head
```

---

### Reverter migration

```bash
alembic downgrade -1
```

---

## Fluxo de desenvolvimento

1. Criar/alterar models
2. Gerar migration
3. Revisar arquivo
4. Rodar `upgrade`
