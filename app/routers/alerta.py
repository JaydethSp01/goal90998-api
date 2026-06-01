from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Alerta(BaseModel):
    id: int
    producto_id: int
    cantidad: int

# Mock database
alertas_db = [
    Alerta(id=1, producto_id=1, cantidad=10),
    Alerta(id=2, producto_id=2, cantidad=5)
]

@router.get("/alerta", response_model=List[Alerta])
async def get_alertas():
    return alertas_db

@router.get("/alerta/{alerta_id}", response_model=Alerta)
async def get_alerta(alerta_id: int):
    for alerta in alertas_db:
        if alerta.id == alerta_id:
            return alerta
    raise HTTPException(status_code=404, detail="Alerta not found")

@router.post("/alerta", response_model=Alerta)
async def create_alerta(alerta: Alerta):
    alertas_db.append(alerta)
    return alerta

@router.put("/alerta/{alerta_id}", response_model=Alerta)
async def update_alerta(alerta_id: int, updated_alerta: Alerta):
    for index, alerta in enumerate(alertas_db):
        if alerta.id == alerta_id:
            alertas_db[index] = updated_alerta
            return updated_alerta
    raise HTTPException(status_code=404, detail="Alerta not found")

@router.delete("/alerta/{alerta_id}")
async def delete_alerta(alerta_id: int):
    for index, alerta in enumerate(alertas_db):
        if alerta.id == alerta_id:
            del alertas_db[index]
            return {"message": "Alerta deleted"}
    raise HTTPException(status_code=404, detail="Alerta not found")
