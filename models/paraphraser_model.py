from pydantic import BaseModel
from enum import Enum
from typing import Union


class ParaphraseMode(str, Enum):
    standard = "standard"
    fluent = "fluent"
    creative = "creative"
    formal = "formal"
    concise = "concise"
    expanded = "expanded"
    humanize = "humanize"
    academic = "academic"
    boomer = "boomer"
    child = "like a 5-year-old child" 
    creative="creative"
    expand="expand"
    shorten="shorten"


class ParaphraseRequest(BaseModel):
    mode: Union[ParaphraseMode, str]  
    input_text: str


class ParaphraseResponse(BaseModel):
    mode: str  
    input_text: str
    paraphrased_text: str
