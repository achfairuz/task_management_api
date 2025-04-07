from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TaskBase (BaseModel):
    description: Optional[str] = None
    status: Optional[str] = 'to-do' 
    category_id: Optional[int]
    
class CreateTask (TaskBase):
    title: str
    category_id: int
    
    

class ResponseTask(TaskBase):
    id: int
    title: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True

class UpdateTask(TaskBase):
    title: Optional[str] = None
 
    category_id: Optional[int] = None
    
   