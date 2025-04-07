from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi_sqlalchemy import db
from models.models import User
from schema.schema_user import  Login, Register
from auth.auth import hash_password, verify_password, create_access_token

routes_auth = APIRouter()

# Login
@routes_auth.post('/login')
def login(payload: Login = Depends(Login.as_form)):
    auth = db.session.query(User).filter(User.username == payload.username).first()
    
    if not auth or not verify_password(payload.password, auth.password):
        raise HTTPException(status_code=401, detail="Not Authorized")
    
    if auth.role == "admin":
        token = create_access_token(data={"sub": auth.username, "role": auth.role})
        return JSONResponse(
        status_code=200,
        content={
            "body": "Login successfully",
            "username": auth.username ,
            "access_token": token,
            "token_type": "bearer"
            }
        )
    else:
        return JSONResponse(
            status_code=200,
            content={
                "body": "Login succesfully",
                "username": auth.username
            }
        )
# Pendaftaran hanya untuk user. Jika ingin masuk sebagai admin, ubah role di database menjadi "admin".
@routes_auth.post('/register')
def register(userRegister: Register = Depends(Register.as_form)):
    existing_username = db.session.query(User).filter(User.username == userRegister.username).first()
    
    if existing_username:
        raise HTTPException(status_code=400, detail="Username is already registered")
    
    hashed_pass = hash_password(userRegister.password)

    
    new_user = User(
        username = userRegister.username,
        password = hashed_pass,
        role = "user"
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return JSONResponse(
        status_code=201,
        content={
        "status": 201,
        "body": {
            "username" : new_user.username,
            },
        "message": "Regsiter succesfull"
         
        }
    )
    
