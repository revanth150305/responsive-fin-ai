from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from query import QueryEngine

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # your frontend tunnel
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    query: str

@app.api_route("/query", methods=["POST", "OPTIONS"])
def handle_query(request: QueryRequest):
    query_engine = QueryEngine()
    response = query_engine.query(request.query)
    return {"answer": response.response}

# @app.api_route("/health", methods=["GET", "OPTIONS"])
# def health_check():
#     return {"status": "ok"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)