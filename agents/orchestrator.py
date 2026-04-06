from agents.planner_agent import generate_study_plan
from db.firestore import save_study_plan

def create_plan(goal: str, days: int):
    plan = generate_study_plan(goal, days)

    data = {
        "goal": goal,
        "days": days,
        "plan": plan
    }

    doc_id = save_study_plan(data)

    return {
        "id": doc_id,
        "goal": goal,
        "days": days,
        "plan": plan
    }