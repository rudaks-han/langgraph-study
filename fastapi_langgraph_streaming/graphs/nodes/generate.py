from typing import Any, Dict

from langgraph.types import StreamWriter

from graphs.chains.generation import generation_chain
from graphs.state import GraphState


async def generate(state: GraphState, writer: StreamWriter) -> Dict[str, Any]:
    print("---GENERATE---")
    question = state["question"]
    documents = state["documents"]

    chunks = []
    async for chunk in generation_chain.astream(
        {"context": documents, "question": question}
    ):
        writer(chunk)
        chunks.append(chunk)

    return {"documents": documents, "question": question, "generation": "".join(chunks)}
