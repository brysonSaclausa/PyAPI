from fastapi import FastAPI

app = FastAPI()

# path operations with FastAPI
@app.get("/")
async def root():
    return {"message": "Hello there!!!"}


@app.get("/posts")
async def root():
    return {"data": "this is a post!!!"}

