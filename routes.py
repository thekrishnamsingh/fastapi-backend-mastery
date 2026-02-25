from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models import Item

router = APIRouter()

# In-memory storage
items = []

@router.get("/items", response_model=List[Item])
def get_items():
    return items


@router.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    for existing_item in items:
        if existing_item.id == item.id:
            raise HTTPException(
                status_code=400,
                detail="Item with this ID already exists"
            )
    items.append(item)
    return {"message": "Item created successfully", "item": item}


@router.get("/items/{item_id}", response_model=Item)
def get_single_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@router.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return {"message": "Item updated successfully"}
    raise HTTPException(status_code=404, detail="Item not found")


@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    for item in items:
        if item.id == item_id:
            items.remove(item)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")