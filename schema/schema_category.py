from pydantic import BaseModel
from typing import Optional
from fastapi import Form


class Kategori(BaseModel):
    
    id: Optional[int]
    name: str

    class Config:
        from_attributes = True  # Pydantic V2 


class KategoriResponse(Kategori):
    pass

class CreateCategory(BaseModel):
    name: str 
    
