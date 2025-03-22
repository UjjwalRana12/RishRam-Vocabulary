from fastapi import APIRouter
from pydantic import BaseModel
from gramformer import Gramformer

router = APIRouter()

gf = Gramformer(models=1, use_gpu=False)

class TextRequest(BaseModel):
    sentence: str

@router.post("/detect")
async def detect_errors(text: TextRequest):
    has_error = gf.detect(text.sentence)
    return {"sentence": text.sentence, "has_error": has_error}

@router.post("/correct")
async def correct_sentence(text: TextRequest):
    corrections = gf.correct(text.sentence)
    return {"sentence": text.sentence, "corrections": list(corrections)}
