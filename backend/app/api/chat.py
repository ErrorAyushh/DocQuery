from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.qa import answer_question

router = APIRouter(prefix="/chat", tags=["Chat"])


class ChatRequest(BaseModel):
    question: str


@router.post("")
def chat(req: ChatRequest):
    return answer_question(req.question)
