from fastapi import FastAPI
from pydantic import BaseModel
from agents.orchestrator import create_plan

from typing import List
from agents.progress_agent import update_progress
from agents.adaptation_agent import adapt_plan

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

class ProgressRequest(BaseModel):
    plan: List[dict]
    completed_day: int

@app.post("/update-progress")
def update_study_progress(request: ProgressRequest):
    updated_plan = update_progress(request.plan, request.completed_day)
    adapted_plan = adapt_plan(updated_plan)

    return {
        "updated_plan": updated_plan,
        "adapted_plan": adapted_plan
    }