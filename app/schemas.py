from pydantic import BaseModel

class VehiculoCreate(BaseModel):
    placa: str
    propietario: str
    marca: str
    fabricacion: int
    valor_comercial: float

class VehiculoResponse(VehiculoCreate):
    impuesto: float
    codigo_revision: str
