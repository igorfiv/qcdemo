from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .find_x import run_calculation

app = FastAPI(title="FastAPI, Docker")

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"hello": "It's a simple API root endpoint"}


@app.get("/calculate/")
async def calculate(value_a: float = 0, value_b: float = 0, target: float = 0, method: str = "fsolve"):
    result = run_calculation(value_a, value_b, target, method)

    return {"result": result}
