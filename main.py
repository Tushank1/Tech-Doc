from fastapi import FastAPI
from database.database import engine,get_db
from fastapi.middleware.cors import CORSMiddleware
from database import db_models


app = FastAPI()

# List of allowed origins (can be specific or allow all with "*")
origins = [
    "http://localhost:5173",  # Frontend URL
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (POST, GET, etc.)
    allow_headers=["*"],  # Allow all headers
)

db_models.Base.metadata.create_all(engine)

@app.get("/")
def About():
    return "Home"