from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from deep_translator import GoogleTranslator

router = APIRouter()

class TranslationRequest(BaseModel):
    text: str
    target_lang: str  


@router.post("/translate")
async def translate_text(request: TranslationRequest):
    try:
        translated_text = GoogleTranslator(source='auto', target=request.target_lang).translate(request.text)
        return {
            "original_text": request.text,
            "translated_text": translated_text,
            "target_language": request.target_lang
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
