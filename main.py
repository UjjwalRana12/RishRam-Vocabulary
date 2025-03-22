from fastapi import FastAPI, HTTPException
from api.paraphraser import router as paraphraser_router
from api.summarizer import router as summarizer_router
from api.grammer import router as grammar_router
from api.translator import router as translator_router 

app = FastAPI(title="Paraphrasing API")

app.include_router(paraphraser_router, prefix="/api")
app.include_router(summarizer_router, prefix="/api")
app.include_router(grammar_router, prefix="/api") 
app.include_router(translator_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Paraphrasing API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8002, reload=True)