from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    """
    Teste simples:
    - Faz GET em /
    - Verifica status 200
    - Confere se a mensagem está correta
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API funcionando com sucesso!"}
