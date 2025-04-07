from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from routes.category import routes_category
from routes.task import routes_task
from routes.auth_routes import routes_auth

import os



app = FastAPI()


app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])
app.include_router(routes_category)
app.include_router(routes_task)
app.include_router(routes_auth)

