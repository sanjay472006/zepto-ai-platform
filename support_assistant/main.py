from fastapi import FastAPI
from models import AskRequest, SupportResponse
from graph import graph


app = FastAPI(
    title="Zepto Support Assistant",
    description="RAG-based Zepto policy support assistant",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Zepto Support Assistant is running"
    }


@app.post("/ask", response_model=SupportResponse)
def ask(request: AskRequest):

    result = graph.invoke({
        "query": request.query,
        "intent": "",
        "answer": "",
        "sources": [],
        "confidence": 0.0
    })

    response = SupportResponse(
        answer=result["answer"],
        sources=result["sources"],
        confidence=result["confidence"]
    )

    return response
