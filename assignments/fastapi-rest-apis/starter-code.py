"""
Task Management API - Starter Code
Build a REST API for managing tasks using FastAPI.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize the FastAPI app
app = FastAPI(title="Task Management API", version="1.0.0")

# TODO: Define a Task model using Pydantic BaseModel
# Properties: id (int), title (str), description (str), completed (bool)
class Task(BaseModel):
    pass


# In-memory storage for tasks (in a real app, use a database)
tasks_db = []
next_task_id = 1


@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to Task Management API"}


# TODO: Implement GET /tasks endpoint
# Should return all tasks
@app.get("/tasks")
def get_tasks():
    pass


# TODO: Implement GET /tasks/{task_id} endpoint
# Should return a specific task by ID or raise HTTPException(404) if not found
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    pass


# TODO: Implement POST /tasks endpoint
# Should accept a Task object and add it to tasks_db
@app.post("/tasks")
def create_task(task: Task):
    pass


# TODO: Implement PUT /tasks/{task_id} endpoint
# Should update an existing task or raise HTTPException(404) if not found
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    pass


# TODO: Implement DELETE /tasks/{task_id} endpoint
# Should delete a task or raise HTTPException(404) if not found
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
