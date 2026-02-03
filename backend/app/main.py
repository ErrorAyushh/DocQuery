from fastapi import FastAPI
from app.api.upload import router as upload_router
from app.api.chat import router as chat_router

app = FastAPI(title="DocQuery API")

app.include_router(upload_router)
app.include_router(chat_router)


@app.get("/")
def health_check():
    return {"status": "DocQuery backend running"}
