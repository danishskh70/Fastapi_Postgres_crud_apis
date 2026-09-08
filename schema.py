

from pydantic import BaseModel


class ItemBase(BaseModel):
    name:str
    description:str
    price:int
    quantity:int

class CreateItem(ItemBase):
    pass

class UpdateItem(ItemBase):
    pass

class DeleteItem(ItemBase):
    pass

class ItemOut(ItemBase):
    id:int
    class Config:
        from_attributes=True