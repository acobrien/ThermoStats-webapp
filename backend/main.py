from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sensor import Sensor

app = FastAPI()

# Enable CORS (for development only!)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Backend is running!"}