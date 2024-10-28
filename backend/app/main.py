from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Your API", version="1.0.0")

# CORS ¼³Á¤
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI backend!"}

@app.get("/api/hello")
async def hello():
    return {"message": "Hello from FastAPI!"}
