from dotenv import load_dotenv

load_dotenv()

from langgraph.graph import END, StateGraph

from graphs.nodes.generate import generate
from graphs.nodes.retrieve import retrieve
from graphs.state import GraphState


workflow = StateGraph(GraphState)

workflow.add_node("retrieve", retrieve)
workflow.add_node("generate", generate)

workflow.set_entry_point("retrieve")
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)

graph_app = workflow.compile()

graph_app.get_graph().draw_mermaid_png(output_file_path="./graph.png")
