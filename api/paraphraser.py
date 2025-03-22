from fastapi import APIRouter
from agents.paraphraser_agent import paraphrase_text
from models.paraphraser_model import ParaphraseRequest, ParaphraseResponse

router = APIRouter()

@router.post("/paraphrase", response_model=ParaphraseResponse)
async def paraphrase(request: ParaphraseRequest):
    
    paraphrased_text = paraphrase_text(request.mode.value, request.input_text)

    return ParaphraseResponse(
        mode=request.mode,
        input_text=request.input_text,
        paraphrased_text=paraphrased_text
    )
