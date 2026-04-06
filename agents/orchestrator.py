from agents.planner_agent import generate_study_plan
from agents.scheduler_agent import create_schedule
from db.firestore import save_study_plan, save_workflow_log

def create_plan(goal: str, days: int):
    workflow_steps = []

    # Step 1: Planner Agent
    plan = generate_study_plan(goal, days)
    workflow_steps.append("planner_agent")

    # Step 2: Scheduler Agent
    schedule = create_schedule(plan)
    workflow_steps.append("scheduler_agent")

    data = {
        "goal": goal,
        "days": days,
        "plan": plan,
        "schedule": schedule
    }

    doc_id = save_study_plan(data)

    # Save workflow log
    log = {
        "goal": goal,
        "agents_called": workflow_steps,
        "status": "completed"
    }

    save_workflow_log(log)

    return {
        "id": doc_id,
        "goal": goal,
        "days": days,
        "plan": plan,
        "schedule": schedule,
        "agents_used": workflow_steps
    }