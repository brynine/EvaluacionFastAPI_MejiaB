from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .database import Base, engine, SessionLocal
from .schemas import VehiculoCreate, VehiculoResponse
from .repository import VehiculoRepository
from .service import VehiculoService
from . import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/vehiculos", response_model=VehiculoResponse)
def registrar_vehiculo(data: VehiculoCreate, db: Session = Depends(get_db)):
    repo = VehiculoRepository(db)
    service = VehiculoService(repo)
    return service.registrar(data)

@app.get("/vehiculos", response_model=list[VehiculoResponse])
def listar_vehiculos(db: Session = Depends(get_db)):
    repo = VehiculoRepository(db)
    service = VehiculoService(repo)
    return service.listar()
