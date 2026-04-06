from agents.planner_agent import generate_study_plan
from agents.scheduler_agent import create_schedule
from db.firestore import save_study_plan

def create_plan(goal: str, days: int):
    # Step 1: Generate plan
    plan = generate_study_plan(goal, days)

    # Step 2: Create schedule
    schedule = create_schedule(plan)

    data = {
        "goal": goal,
        "days": days,
        "plan": plan,
        "schedule": schedule
    }

    doc_id = save_study_plan(data)

    return {
        "id": doc_id,
        "goal": goal,
        "days": days,
        "plan": plan,
        "schedule": schedule
    }