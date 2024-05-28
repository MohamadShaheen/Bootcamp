import uvicorn
from fastapi import FastAPI
from routers import pokemons_router, evolve_router, functions, trainers_router

host = '127.0.0.1'
port = 8000

app = FastAPI()


app.include_router(pokemons_router.router, prefix='/pokemons')
app.include_router(trainers_router.router, prefix='/trainers')
app.include_router(evolve_router.router, prefix='/evolve')

@app.get('/')
def root():
    return f'Are you that Naive and old fashion? Go to {host}:{port}/docs for better experience'
