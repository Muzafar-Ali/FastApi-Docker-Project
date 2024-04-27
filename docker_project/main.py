from fastapi import FastAPI
from sqlmodel import SQLModel, Field, Session, create_engine, select
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=100, nullable=False)
    secret_name: str
    age: int | None = None

# Use the DATABASE_URL environment variable
connection_string = os.getenv("DATABASE_URL")
engine = create_engine(connection_string, echo=True) # type: ignore

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("creatitng tables.. lifespan start")
    create_db_and_tables()
    yield
    print("lifespan end")

app: FastAPI = FastAPI(
    lifespan=lifespan,
    title="API for Docker connection",
    description="this is api is created to run on docker",
)

def get_session():
    with Session(engine) as session:
        yield session

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/heroes")
def create_hero(hero: Hero):
    with Session(engine) as session:
        session.add(hero)
        session.commit()
        session.refresh(hero)
        return hero

@app.get("/heroes")
def read_heroes():
    with Session(engine) as session:
        statement = select(Hero)
        heroes = session.exec(statement).all()
        return heroes