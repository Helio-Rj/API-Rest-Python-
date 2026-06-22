from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_list_tasks_returns_list():
    """
    Teste didático:
    - Faz GET em /tasks
    - Verifica status 200
    - Garante que o retorno é uma lista
    """
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
