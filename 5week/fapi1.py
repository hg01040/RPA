from fastapi import FastAPI

app = FastAPI()

@app.get("/") #  app.get하고 함수식으로 API 생성
def read_root(): #
    return {"Hello": "World"} #

@app.get("/item")
def read_item(item_id: int, name: str = None, age: int = 0):
    return {"item_id": item_id, "name": name, "age": age}