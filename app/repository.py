from sqlalchemy.orm import Session
from .models import Vehiculo

class VehiculoRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, vehiculo: Vehiculo):
        self.db.add(vehiculo)
        self.db.commit()
        self.db.refresh(vehiculo)
        return vehiculo

    def get_all(self):
        return self.db.query(Vehiculo).all()
