from typing import List, Dict

def generate_study_plan(goal: str, days: int) -> List[Dict]:
    topics = [
        "Basics",
        "Arrays",
        "Linked List",
        "Stacks & Queues",
        "Trees",
        "Graphs",
        "Revision"
    ]

    plan = []
    for i in range(days):
        topic = topics[i % len(topics)]
        plan.append({
            "day": i + 1,
            "topic": topic
        })

    return plan