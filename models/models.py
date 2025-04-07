from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import ENUM 


Base = declarative_base()


status_enum = ENUM('to-do', 'in-progress', 'done', name='statusenum', create_type=False) 


class Kategori(Base):
    __tablename__ = 'kategori'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Tugas(Base):
    __tablename__ = 'tugas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(status_enum, nullable=False, server_default='to-do')
    category_id = Column(Integer, ForeignKey('kategori.id'), nullable= False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    category = relationship('Kategori')


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True, autoincrement=True,index=True)
    username = Column(String,nullable=False,index=True)
    password = Column(String,nullable=False)
    role = Column(String, default="user", nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())