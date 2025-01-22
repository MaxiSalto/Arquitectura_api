from fastapi import FastAPI
from routers import users, admin, general

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(general.router, prefix="/general", tags=["General"])

@app.get("/")
def root():
    return {"message": "Welcome to the API Architecture!"}
