from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Stock(BaseModel):
    id: int
    producto_id: int
    cantidad: int
    talla_id: int

# Mock database
stocks_db = [
    Stock(id=1, producto_id=1, cantidad=100, talla_id=1),
    Stock(id=2, producto_id=2, cantidad=50, talla_id=2)
]

@router.get("/stock", response_model=List[Stock])
async def get_stocks():
    return stocks_db

@router.get("/stock/{stock_id}", response_model=Stock)
async def get_stock(stock_id: int):
    for stock in stocks_db:
        if stock.id == stock_id:
            return stock
    raise HTTPException(status_code=404, detail="Stock not found")

@router.post("/stock", response_model=Stock)
async def create_stock(stock: Stock):
    stocks_db.append(stock)
    return stock

@router.put("/stock/{stock_id}", response_model=Stock)
async def update_stock(stock_id: int, updated_stock: Stock):
    for index, stock in enumerate(stocks_db):
        if stock.id == stock_id:
            stocks_db[index] = updated_stock
            return updated_stock
    raise HTTPException(status_code=404, detail="Stock not found")

@router.delete("/stock/{stock_id}")
async def delete_stock(stock_id: int):
    for index, stock in enumerate(stocks_db):
        if stock.id == stock_id:
            del stocks_db[index]
            return {"message": "Stock deleted"}
    raise HTTPException(status_code=404, detail="Stock not found")
