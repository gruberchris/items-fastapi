from fastapi import FastAPI, HTTPException

app = FastAPI()

items = []


@app.get("/items")
async def read_items(limit: int = 10) -> list[str]:
    return items[:limit]


@app.get("/items/{item_id}")
async def read_item(item_id: int) -> str:
    if item_id >= len(items):
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found.")

    return items[item_id]


@app.post("/items")
async def create_item(item: str) -> str:
    items.append(item)
    return item


@app.delete("/items")
async def delete_item(item: str) -> str:
    if item not in items:
        raise HTTPException(status_code=404, detail=f"Item {item} not found.")

    items.remove(item)
    return item


@app.put("/items")
async def update_item(item: str, new_item: str) -> str:
    if item not in items:
        raise HTTPException(status_code=404, detail=f"Item {item} not found.")

    items.remove(item)
    items.append(new_item)
    return new_item
