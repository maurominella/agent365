import uvicorn
# test with:
# curl -X POST http://127.0.0.1:8000/echo -H "Content-Type: application/json" -d "{\"message\": \"ciao\"}"


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Pydantic models, e.g. data models for request and response bodies
class EchoRequest(BaseModel):
    message: str

class EchoResponse(BaseModel):
    echo: str

# Example usages of Pydantic model instantiation
my_dict = {"echo": "Dict1"}
x = EchoResponse(echo="Test")
y = EchoResponse(**my_dict)
z = EchoResponse(**{"echo": "Dict2"})


@app.post("/echo", response_model=EchoResponse)
def echo(req: EchoRequest):
    return EchoResponse(echo=f"Hai detto: {req.message}")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=80,
        reload=True
    )
