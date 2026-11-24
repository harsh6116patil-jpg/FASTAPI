from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos =[]
class Todo(BaseModel):
    task : str
    id : int 
    completed:bool

@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {"message":"Todo added",
            "data" : todo}

@app.get("/get_todos")
def see_todos():
    return todos

@app.get("/get_todos/{user_id}")
def see_todo_id(user_id:int):
    for i in todos :
        if i.id == user_id:
            return i
    return {"Error" : "todo not found"}

@app.put("/update_todo/{todo_id}")
def update_todo(updated_todo:Todo,todo_id:int):
    for index,i in enumerate(todos):
        if i.id == todo_id :
            todos[index] = updated_todo
            return {"Message" :"Todo Updated",
                    "data" : updated_todo}
    return {"error":"Data not found"}

@app.delete("/delete_todo/{todo_id}")
def delete_todo(todo_id:int):
    for index,i in enumerate(todos):
        if i.id == todo_id:
            todos[index].pop()
            return {"Message":"Data removed"}
    return {"error":"Data not found"}