from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi_sqlalchemy import db
from models.models import Kategori as ModelKategori
from schema.schema_category import CreateCategory, KategoriResponse
from auth.auth import get_current_user
routes_category = APIRouter()

@routes_category.get('/categories')
def list_categories():
    categories = db.session.query(ModelKategori).all()
    

    return JSONResponse(
        status_code=200,
        content={"status": 200, "body": jsonable_encoder(categories)}
    )

@routes_category.post('/categories')
def create_category(payload: CreateCategory ,current_user: dict = Depends(get_current_user)):
    
    new_category = ModelKategori(name=payload.name)
    db.session.add(new_category)
    db.session.commit()
    db.session.refresh(new_category)

    result = KategoriResponse.model_validate(new_category).model_dump()
    
    return JSONResponse(
        status_code=200,
        content={"status": 200, "body": result }
    )
