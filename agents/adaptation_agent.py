from typing import List, Dict

def adapt_plan(plan: List[Dict]) -> List[Dict]:
    adapted_plan = []

    delay = 0

    for item in plan:
        if item.get("status") == "pending":
            adapted_plan.append({
                "day": item["day"] + delay,
                "topic": item["topic"],
                "status": "rescheduled"
            })
            delay += 1
        else:
            adapted_plan.append(item)

    return adapted_plan