# main.py
from fastapi import FastAPI

# 创建 FastAPI 实例
app = FastAPI()

# 定义一个根路由
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# 带路径参数的路由
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}