from fastapi import FastAPI
from pydantic import BaseModel
from agents.orchestrator import create_plan

app = FastAPI()

class PlanRequest(BaseModel):
    goal: str
    days: int

@app.get("/")
def root():
    return {"message": "Adaptive Learning Orchestrator API"}

@app.post("/create-plan")
def create_study_plan(request: PlanRequest):
    result = create_plan(request.goal, request.days)
    return result