 em Python com FastAPI

Este projeto é uma API desenvolvida em **FastAPI** com testes automatizados via **GitHub Actions**.

---

## 📦 Instalação

```bash
# Clone o repositório
git clone <url-do-repo>
cd nome-do-projeto

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Instale as dependências
pip install -r requirements.txt
▶️ Execução
bash
uvicorn app.main:app --reload
A aplicação estará disponível em: http://127.0.0.1:8000/ (127.0.0.1 in Bing)

Documentação interativa: http://127.0.0.1:8000/docs (127.0.0.1 in Bing)

🧪 Testes
bash
pytest
Os testes garantem que os endpoints funcionam corretamente.

O pipeline roda automaticamente no GitHub Actions a cada PR.

📂 Estrutura do Projeto
Código
.
├── app/
│   └── main.py
├── tests/
│   └── test_root.py
├── requirements.txt
└── README.md
✅ Status
Pipeline configurado e rodando com sucesso

Branch principal protegida

Testes automatizados ativos

✨ Contribuição
Crie uma branch de feature:

bash
git checkout -b feature/nome-da-feature
Faça suas alterações e commit:

bash
git commit -m "Descrição clara da mudança"
Abra um Pull Request para main.

📖 Licença
Este projeto está sob a licença MIT.
Sinta‑se livre para usar, modificar e contribuir.
