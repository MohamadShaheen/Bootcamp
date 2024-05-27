import uvicorn
from fastapi import FastAPI
from routers import get_router, post_router, delete_router

host = '127.0.0.1'
port = 8000

app = FastAPI()


app.include_router(get_router.router)
app.include_router(post_router.router)
app.include_router(delete_router.router)


@app.get('/')
def root():
    return f'Are you that Naive and old fashion? Go to {host}:{port}/docs for better experience'
