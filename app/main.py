from fastapi import FastAPI

app = FastAPI()

# Dados em memória só para teste
tasks = [
    {"id": 1, "title": "Estudar API REST", "done": False},
    {"id": 2, "title": "Fazer exercício", "done": True}
]


@app.get("/tasks")
def get_tasks():
    return tasks
