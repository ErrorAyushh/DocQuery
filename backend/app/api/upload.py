import shutil
from fastapi import APIRouter, UploadFile, File

from app.rag.loader import load_pdf
from app.rag.splitter import split_documents
from app.rag.vectorstore import index_chunks

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    documents = load_pdf(file_path)
    chunks = split_documents(documents)

    # 🔥 NEW: index chunks into Qdrant
    index_chunks(chunks)

    return {
        "filename": file.filename,
        "pages_loaded": len(documents),
        "chunks_created": len(chunks)
    }
