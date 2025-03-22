# agents/summarization_agent.py - Update with better debugging
import re
import google.generativeai as genai
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Loading environment variables...")
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    logger.error("Google API Key is missing! Check your .env file.")
    raise ValueError("Google API Key is missing! Check your .env file.")
else:
    logger.info("API key loaded successfully (first 4 chars): " + api_key[:4] + "...")

class SummarizationAgent:
    def __init__(self):
        logger.info("Initializing SummarizationAgent...")
        try:
            genai.configure(api_key=api_key)
            self.llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
            logger.info("Google Generative AI configured successfully")
            
            self.prompt = PromptTemplate.from_template("Summarize this: {text}")
            logger.info("Prompt template created")
            
            self.summarization_chain = RunnableSequence(self.prompt | self.llm)
            logger.info("Summarization chain created successfully")
        except Exception as e:
            logger.error(f"Error during initialization: {str(e)}")
            raise

    def preprocess_text(self, text: str) -> str:
        """Clean the text by removing special and control characters."""
        logger.info(f"Preprocessing text (length: {len(text)})")
        text = text.replace("\n", " ").replace("\r", "").strip()
        text = re.sub(r"[^\x20-\x7E]", "", text)
        text = re.sub(r"\\", "", text)
        return text[:1024]

    def summarize(self, text: str) -> str:
        """Summarize the given text using Google Gemini API."""
        logger.info(f"Starting summarization of text (length: {len(text)})")
        try:
            cleaned_text = self.preprocess_text(text)
            logger.info(f"Text preprocessed (length: {len(cleaned_text)})")

            if not cleaned_text.strip():
                logger.error("Input text is empty after preprocessing")
                raise ValueError("Input text cannot be empty or invalid.")

            logger.info("Invoking summarization chain")
            result = self.summarization_chain.invoke({"text": cleaned_text})
            logger.info("Summarization completed successfully")
            
            if isinstance(result, str):
                return result
            # Handle LangChain's response object
            elif hasattr(result, 'content'):
                return result.content
            else:
                logger.warning(f"Unexpected result type: {type(result)}")
                return str(result)
        except Exception as e:
            logger.error(f"Error during summarization: {str(e)}")
            raise