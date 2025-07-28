from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tasks = []

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

@app.get("/")
def home():
    return {"message": "Добро пожаловать на главную страничку"}

@app.post('/tasks')
def add_task(new_task: Task):
    tasks.append(new_task)
    return {"message": "Задание добавленно"}

@app.get('/tasts')
def get_tasks():
    return {"Задание": tasks}