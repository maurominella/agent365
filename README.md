# Echo Agent – FastAPI + Uvicorn + Docker + UV

A minimal Echo Agent built with FastAPI.  
It exposes a simple `/echo` endpoint and serves as a base for experimenting with local development, containerization, and future integration with Teams/Copilot.

---

## 🚀 Local Development

### Start FastAPI (development mode)

Since the project uses an inline launcher:

```python
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
```

Now you can simply run `python main.py`

## Test with curl
```
curl -X POST http://127.0.0.1:8000/echo \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"Hello world!\"}"
```

## Swagger UI
```
http://127.0.0.1:8000/docs
```

## Python Environment with UV
- On Linux / MAC --> `curl -LsSf https://astral.sh/uv/install.sh | sh`
- On Windows --> `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

### Environment preparation
- *CD* into the folder
- Create the environment: `uv init . --python 3.13`.
- Add libraries (bad method): `uv add python-dotenv fastapi uvicorn`.
- Add libraries (better method): `uv add $(cat requirements.txt)`.
- Syncrhonize to create the file structure: `uv sync`.
- Activate the environment:
  - on Linux/MC --> `source .venv/bin/activate`.
  - on Windows --> `.venv\Scripts\activate.ps1`.
- To deactivate --> `deactivate`.

## Docker
Build the image:
```
docker build -t echo-agent:latest .
```

Run locally:
```
docker run -p 8080:80 echo-agent:latest
```

Swagger inside the container:
```
http://localhost:8080/docs
```

## API Endpoint

POST /echo
```
{ "message": "test" }
```
Response:
```
{ "echo": "You said: test" }
```