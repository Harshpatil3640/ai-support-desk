"""AI Support Desk API: creates the FastAPI application."""

from fastapi import FastAPI

app = FastAPI(
    title="AI Support Desk API",
    description="Support ticket system that uses machine learning to route tickets.",
    version="0.1.0",
)


@app.get("/api/health", tags=["system"])
def health_check() -> dict[str, str]:
    """Check that the API is running."""
    return {"status": "ok", "app": "AI Support Desk", "version": app.version}