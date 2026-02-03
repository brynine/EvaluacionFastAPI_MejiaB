from fastapi import HTTPException
from .models import Vehiculo

class VehiculoService:

    def __init__(self, repository):
        self.repository = repository

    def registrar(self, data):
        if len(data.placa) < 4 or data.placa[3] != "-":
            raise HTTPException(status_code=400, detail="Placa inválida")

        base = data.valor_comercial * 0.025

        if data.fabricacion < 2010:
            base += base * 0.10

        if data.marca[0].lower() in "aeiou":
            base -= 30

        impuesto = max(base, 0)

        codigo_revision = (
            data.placa[:3]
            + str(len(data.propietario))
            + str(data.fabricacion)[-1]
        )

        vehiculo = Vehiculo(
            placa=data.placa,
            propietario=data.propietario,
            marca=data.marca,
            fabricacion=data.fabricacion,
            valor_comercial=data.valor_comercial,
            impuesto=impuesto,
            codigo_revision=codigo_revision
        )

        return self.repository.create(vehiculo)

    def listar(self):
        return self.repository.get_all()
