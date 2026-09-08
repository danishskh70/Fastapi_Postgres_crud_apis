

from sqlalchemy.orm import Session

import model
import schema


def get_item(db:Session,item_id:int):
    return db.query(model.Item).filter(model.Item.id==item_id).first()

def get_items(db:Session,skip:int=0,limit:int=10):
    return db.query(model.Item).offset(skip).limit(limit).all()

def create_item(db:Session,item:schema.CreateItem):
    db_item =model.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db:Session,item_id:int,item:schema.UpdateItem):
    db_item=get_item(db,item_id)
    if not db_item:
        return None
    for key,value in item.model_dump().items():
        setattr(db_item,key,value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db:Session,item_id:int):
    db_item =get_item(db,item_id)
    if not db_item:
        return None
    db.delete(db_item)
    db.commit()
    return db_item


