from fastapi import FastAPI
from starlette.responses import StreamingResponse

from graphs.graph import graph_app

app = FastAPI()


@app.get("/search")
async def search(query: str):
    async def event_stream():
        try:
            async for chunk in graph_app.astream(
                input={"question": query},
                stream_mode=[
                    "custom",
                ],
            ):

                yield f"data: {chunk[1]}\n\n"
        except Exception as e:
            yield f"data: {str(e)}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")
