from fastapi import APIRouter
from app.models.schema import SummarizeRequest, SummarizeResponse
from app.services.summarizer import summarize_text
from app.core.config import settings

router = APIRouter()

@router.post("/summarize", response_model=SummarizeResponse)
def summarize(request: SummarizeRequest):
    summary = summarize_text(request.text, request.length)
    return SummarizeResponse(summary=summary, model_used=settings.model)