from typing import Any, Dict

from graphs.state import GraphState
from ingestion import retriever


async def retrieve(state: GraphState) -> Dict[str, Any]:
    print("---RETRIEVE---")
    question = state["question"]

    documents = await retriever.ainvoke(question)
    return {"documents": documents, "question": question}
