from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os


load_dotenv()


model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')


def paraphrase_text(mode: str, input_text: str) -> str:
    prompt = f"Paraphrase the following text in {mode} mode:\n\n{input_text}"
    
    result = model.invoke(prompt)
    return result.content
