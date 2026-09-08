from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

import crud
import database
import model
import schema

# postgresql_url="postgresql://root:root@localhost/conn"
app=FastAPI()
model.Base.metadata.create_all(bind=database.engine)

# engine =create_engine(postgresql_url)
# SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
# Base=declarative_base()

# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


@app.get("/")
def root():
    return {"message":"HomePage"}

@app.get('/item/{item_id}',response_model=schema.ItemOut)
def read_item(item_id:int,db:Session=Depends(database.get_db)):
    db_item=crud.get_item(db,item_id=item_id)
    if not db_item:
        raise HTTPException(status_code=404,detail="Item not Found")
    return db_item

@app.get("/items/")
def get_items(db:Session=Depends(database.get_db),skip:int=0,limit:int=10):
    return crud.get_items(db=db,skip=skip,limit=limit)

@app.post("/item/",response_model=schema.ItemOut)
def create_item(item:schema.CreateItem,db:Session=Depends(database.get_db)):
    return crud.create_item(db=db,item=item)

@app.put("/item/{item_id}",response_model=schema.ItemOut)
def update_item(item_id:int,item:schema.UpdateItem,db:Session=Depends(database.get_db)):
    db_item=crud.update_item(db=db,item_id=item_id,item=item)
    if not db_item:
        raise HTTPException(status_code=404 , detail="Item not Found")
    return db_item

@app.delete("/item/{item_id}",response_model=schema.ItemOut)
def delete_item(item_id:int ,db:Session=Depends(database.get_db)):
    db_item=crud.delete_item(db=db,item_id=item_id)
    if not db_item:
        raise HTTPException(status_code=404,detail="Item not Found")
    return db_item 