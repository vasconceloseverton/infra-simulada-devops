
# 🚀 Infra Simulada DevOps

Este projeto é uma aplicação simples em Flask, criada para fins de simulação de infraestrutura DevOps, CI/CD, monitoramento e automações.  
A aplicação está hospedada no Render, com deploy automatizado via GitHub Actions e sistema de monitoramento com alerta no Telegram.

---

## 📦 Tecnologias Utilizadas
- Python + Flask
- GitHub Actions (CI/CD)
- Docker
- Render (Deploy Cloud)
- Monitoramento via Healthcheck + Telegram Bot

---

## 🏗️ Estrutura do Projeto

```
.
├── app/
│   └── app.py
├── scripts/
│   ├── healthcheck.py
│   └── healthcheck_with_alert.py
├── Dockerfile
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── requirements.txt
└── README.md
```

---

## 🚀 Deploy no Render

### ✅ Build Command
```
pip install -r requirements.txt && python app/app.py
```

### ✅ Start Command
```
python app/app.py
```

### ✅ Deploy Manual pelo Render
1. Crie um novo Web Service no Render.
2. Configure o repositório GitHub.
3. Use o comando acima como Start Command.

---

## 🤖 Configurar Bot no Telegram para Alerta

1. No Telegram, busque `@BotFather` e crie um bot com `/newbot`.
2. Pegue o Token fornecido.
3. Obtenha seu Chat ID acessando:
```
https://api.telegram.org/bot<SEU_TOKEN>/getUpdates
```
4. Anote o Chat ID e o Token.

---

## 🩺 Script de Monitoramento

O script `scripts/healthcheck_with_alert.py` verifica se a aplicação está online.  
Se não estiver, envia uma mensagem de alerta no Telegram.

### ✅ Executar manualmente:
```bash
export TELEGRAM_TOKEN="seu_token"
export TELEGRAM_CHAT_ID="seu_chat_id"
python scripts/healthcheck_with_alert.py https://sua-url.onrender.com
```

---

## 🔗 CI/CD com GitHub Actions

Pipeline configurado em `.github/workflows/ci-cd.yml`.

### 🔐 Secrets necessários no GitHub:
- `RENDER_API_KEY`
- `RENDER_SERVICE_ID`
- `TELEGRAM_TOKEN`
- `TELEGRAM_CHAT_ID`

### 📜 Fluxo:
1. Faz checkout do repositório.
2. Instala dependências.
3. Faz deploy no Render.
4. Aguarda o deploy subir.
5. Executa healthcheck.
6. Se falhar ➝ Envia alerta no Telegram.

---

## 🐳 Docker

### ✅ Build da imagem:
```bash
docker build -t flask-app .
```

### ✅ Executar:
```bash
docker run -d -p 5000:5000 flask-app
```

---

## 📄 License

MIT License - livre para uso educacional e profissional.
