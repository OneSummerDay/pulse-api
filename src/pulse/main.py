from fastapi import FastAPI


app = FastAPI(
    title="Pulse API",
    version="0.1.0",
    description="API monitoring and uptime tracking service",
)

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
