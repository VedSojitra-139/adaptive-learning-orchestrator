from agents.planner_agent import generate_study_plan

def create_plan(goal: str, days: int):
    plan = generate_study_plan(goal, days)
    
    return {
        "goal": goal,
        "days": days,
        "plan": plan
    }