# api/summarizer.py - Modified with better error handling
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import traceback
import sys
from agents.summarization_agent import SummarizationAgent

router = APIRouter()

try:
    # Print debugging info about module loading
    print("Loading summarization agent...")
    summarization_agent = SummarizationAgent()
    print("Summarization agent loaded successfully")
except Exception as e:
    print(f"Error initializing summarization agent: {str(e)}")
    traceback.print_exc()
    # Create a dummy agent that will give more helpful errors
    class DummySummarizationAgent:
        def summarize(self, text):
            return f"Agent initialization failed: {str(e)}"
    summarization_agent = DummySummarizationAgent()

class SummarizationRequest(BaseModel):
    text: str

class SummarizationResponse(BaseModel):
    summary: str

@router.post("/summarize", response_model=SummarizationResponse)
def summarize_text(request: SummarizationRequest):
    """Endpoint to summarize text."""
    try:
        if not request.text.strip():
            raise ValueError("Input text is empty or invalid.")
        
        print(f"Received text: {request.text[:50]}...")  # Print first 50 chars
        summary = summarization_agent.summarize(request.text)
        print(f"Summary generated: {summary[:50]}...")  # Print first 50 chars
        return SummarizationResponse(summary=summary)
    except ValueError as e:
        print(f"Validation error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        error_msg = f"Summarization error: {str(e)}"
        print(error_msg)
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=error_msg)