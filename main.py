"""
Setu prototype entrypoint.

Runs a lightweight FastAPI app that will expose the orchestrator so signals
can be posted in and routed through the agent pipeline. Kept minimal for
week 1 of the 30-day plan: get a signal in, routed, and gated.
"""

from fastapi import FastAPI
from pydantic import BaseModel

from agents.orchestrator import OrchestratorAgent

app = FastAPI(title="Setu Prototype")
orchestrator = OrchestratorAgent()


class Signal(BaseModel):
    source: str  # "transaction" | "bc_field_activity" | "app_usage"
    payload: dict


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/signal")
def receive_signal(signal: Signal) -> dict:
    """
    Entry point for a new signal. Hands off to the orchestrator agent.
    """
    # TODO: once OrchestratorAgent.handle_signal is implemented, call it here
    # return orchestrator.handle_signal(signal.dict())
    return {"received": signal.dict()}
