from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)
    completed: bool = False


class Task(TaskCreate):
    id: int


tasks = [
    {"id": 1, "title": "Learn FastAPI", "completed": False},
    {"id": 2, "title": "Build a REST API", "completed": True},
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/tasks")
def get_tasks(completed: bool | None = Query(default=None)):
    # TODO: filter tasks if completed is provided
    return tasks


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    # TODO: create a new task and append it to the list
    return {"message": "Task created"}


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: find task by id and return it or raise 404
    return {"message": "Task details"}


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate):
    # TODO: update the task and return the new version
    return {"message": "Task updated"}


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    # TODO: remove the task and return no content
    return None
