from fastapi import FastAPI

from routers.app import router as app_router

app =FastAPI()
app.include_router(app_router)

@app.get("/")
def root():
    return {"message": "Welcome to the subscriber management app."}