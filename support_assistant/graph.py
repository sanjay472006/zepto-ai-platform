import os

from langgraph.graph import StateGraph, START, END

from models import GraphState
from rag import retrieve_documents


def classify_intent(state: GraphState):
    query = state["query"].lower()

    keywords = [
        "delivery",
        "return",
        "refund",
        "membership",
        "tracking",
        "cancel",
        "gift card",
        "support hours"
    ]

    if any(keyword in query for keyword in keywords):
        return {
            "intent": "policy_question"
        }

    return {
        "intent": "general_question"
    }


def retrieve_and_answer(state: GraphState):
    query = state["query"]

    results = retrieve_documents(query, top_k=3)

    documents = results["documents"][0]
    ids = results["ids"][0]

    if not documents:
        return {
            "answer": "No relevant policy information was found.",
            "sources": [],
            "confidence": 1.0
        }

    top_chunk = documents[0]

    mock_llm = os.getenv("MOCK_LLM", "1")

    if mock_llm == "1":
        answer = (
            "Based on the retrieved context: "
            + top_chunk[:200]
        )
    else:
        # Optional real LLM path will be added later.
        answer = (
            "Based on the retrieved context: "
            + top_chunk[:200]
        )

    return {
        "answer": answer,
        "sources": ids,
        "confidence": 1.0
    }


def direct_answer(state: GraphState):
    mock_llm = os.getenv("MOCK_LLM", "1")

    if mock_llm == "1":
        answer = (
            "I can only answer questions about "
            "Zepto policies right now."
        )
    else:
        # Optional real LLM path will be added later.
        answer = (
            "I can only answer questions about "
            "Zepto policies right now."
        )

    return {
        "answer": answer,
        "sources": [],
        "confidence": 1.0
    }


def route_question(state: GraphState):
    if state["intent"] == "policy_question":
        return "retrieve_and_answer"

    return "direct_answer"


builder = StateGraph(GraphState)

builder.add_node(
    "classify_intent",
    classify_intent
)

builder.add_node(
    "retrieve_and_answer",
    retrieve_and_answer
)

builder.add_node(
    "direct_answer",
    direct_answer
)

builder.add_edge(
    START,
    "classify_intent"
)

builder.add_conditional_edges(
    "classify_intent",
    route_question,
    {
        "retrieve_and_answer": "retrieve_and_answer",
        "direct_answer": "direct_answer"
    }
)

builder.add_edge(
    "retrieve_and_answer",
    END
)

builder.add_edge(
    "direct_answer",
    END
)

graph = builder.compile()


if __name__ == "__main__":

    print("\n===== TEST 1: POLICY QUESTION =====")

    result = graph.invoke({
        "query": "How much does Zepto charge for delivery?",
        "intent": "",
        "answer": "",
        "sources": [],
        "confidence": 0.0
    })

    print(result)

    print("\n===== TEST 2: GENERAL QUESTION =====")

    result = graph.invoke({
        "query": "What is artificial intelligence?",
        "intent": "",
        "answer": "",
        "sources": [],
        "confidence": 0.0
    })

    print(result)
