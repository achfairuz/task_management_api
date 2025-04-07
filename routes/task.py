from fastapi import APIRouter, HTTPException,Query
from fastapi.responses import JSONResponse
from fastapi_sqlalchemy import db
from fastapi.encoders import jsonable_encoder
from models.models import Tugas as task, Kategori as category
from schema.schema_task import CreateTask,UpdateTask
from typing import Optional


routes_task = APIRouter()


# CREATE TASK
@routes_task.post('/tasks' )
def create_task(payload: CreateTask ):
    category_id = db.session.query(category).filter(category.id == payload.category_id).first()
    
    if not category_id:
        raise HTTPException(status_code=404,detail="ID Category Not Found")
    
    
    VALID_STATUSES = ['to-do', 'in-progress', 'done']

    if payload.status not in VALID_STATUSES:
        raise HTTPException(
        status_code=400,
        detail=f"Status '{payload.status}' Invalid. No tasks found {', '.join(VALID_STATUSES)}"
    )
        
    new_task = task(
        title=payload.title,
        description=payload.description,
        status=payload.status,
        category_id=payload.category_id
    )
    db.session.add(new_task)
    db.session.commit()
    db.session.refresh(new_task)
    
    
    return JSONResponse(
        status_code=201,
        content={
            "status": 201,
            "body": jsonable_encoder(new_task) 
        }
    )

# READ BASED ON ID
@routes_task.get('/tasks/{id}')
def get_task(id: int):
    existing_task = db.session.query(task).filter(task.id == id).first()
    
    if not existing_task:
        raise HTTPException(status_code=404, detail="ID NOT FOUND")

    return JSONResponse(
        status_code=200,
        content={
                "status": 200,
                "body": jsonable_encoder(existing_task)
                }
        )
# READ ALL OR ALSO BASED ON STATUS OR CATEGORY_ID
@routes_task.get('/tasks')
def get_task_all(status: Optional[str] = None, category_id: Optional[str] = None, 
                page: Optional[int] = Query(1, ge=1), 
                per_page: Optional[int] = Query(10, ge=1, le=100), 
    ):
    VALID_STATUSES = ['to-do', 'in-progress', 'done']


    if status and status not in VALID_STATUSES:
        raise HTTPException(
            status_code=400,
            detail=f"Status '{status}' Invalid. Use one of the following: {', '.join(VALID_STATUSES)}"
        )


    query = db.session.query(task)
    if status:
        query = query.filter(task.status == status)
        
    if category_id:
        check_category = db.session.query(task).filter(task.category_id == category_id).all()
        if not check_category:
            raise HTTPException(
                status_code=404,
                detail="Data Not Found"
            )
        query = query.filter(task.category_id == category_id)
    
   
    
    task_count = query.count()
    
    paginated_tasks =query.offset((page - 1)*per_page).limit(per_page).all()
    
    total_pages = (task_count + per_page - 1) // per_page
    
    if not paginated_tasks:
        raise HTTPException(status_code=404, detail="No Tasks Found")


    return JSONResponse(
        status_code=200,
        content={
                "status": 200,
                "body": jsonable_encoder(paginated_tasks),
                "pagination": {
                    "total_tasks": task_count,
                    "total_pages": total_pages,
                    "current_page": page,
                    "per_page": per_page 
                    
                }
                }
    )

# UPDATE TASK
@routes_task.put('/tasks/{id}')
def update_task(id: int, payload: UpdateTask ):
    existing_task = db.session.query(task).filter(task.id == id).first()
    
    if not existing_task:
        raise HTTPException(status_code=404, detail='ID Task Not Found')
    
    if payload.category_id:
        existing_category = db.session.query(category).filter(category.id == payload.category_id).first()
        if not existing_category:
            raise HTTPException(status_code=404, detail="ID Category Not Found")
    
    
    VALID_STATUSES = ['to-do', 'in-progress', 'done']

    if payload.title is not None:
        existing_task.title = payload.title
    if payload.description is not None:
        existing_task.description = payload.description
    if payload.status is not None:
        if payload.status not in VALID_STATUSES:
            raise HTTPException(status_code=400, detail=f"Status '{payload.status}' Invalid")
        existing_task.status = payload.status
    if payload.category_id is not None:
        existing_task.category_id = payload.category_id

    db.session.commit()
    db.session.refresh(existing_task)
    return JSONResponse(status_code=200,
                        content={
                            "status": 200,
                            "body": jsonable_encoder(existing_task)
                        })
    

# DELETE TASK
@routes_task.delete('/tasks/{id}')
def delete_task(id: int):
    existing_task = db.session.query(task).filter(task.id == id).first()
    
    if not existing_task:
        raise HTTPException(status_code=404, detail="ID NOT FOUND")

    db.session.delete(existing_task)
    db.session.commit()
    
    return JSONResponse(
        status_code=200,
        content={
            "status": 200,
            "body": "Data has been successfully deleted"
        }
    )
    
