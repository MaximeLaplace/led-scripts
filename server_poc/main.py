from a2wsgi import ASGIMiddleware
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


application = ASGIMiddleware(app)
