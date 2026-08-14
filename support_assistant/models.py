from typing import TypedDict
from pydantic import BaseModel, Field


class GraphState(TypedDict):
    query: str
    intent: str
    answer: str
    sources: list[str]
    confidence: float


class SupportResponse(BaseModel):
    answer: str
    sources: list[str]
    confidence: float = Field(ge=0.0, le=1.0)


class AskRequest(BaseModel):
    query: str
