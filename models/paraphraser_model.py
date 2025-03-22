from pydantic import BaseModel
from enum import Enum


class ParaphraseMode(str, Enum):
    standard = "standard"
    fluent = "fluent"
    creative = "creative"
    formal = "formal"
    concise = "concise"
    expanded = "expanded"
    humanize = "humanize"


class ParaphraseRequest(BaseModel):
    mode: ParaphraseMode
    input_text: str


class ParaphraseResponse(BaseModel):
    mode: ParaphraseMode
    input_text: str
    paraphrased_text: str
