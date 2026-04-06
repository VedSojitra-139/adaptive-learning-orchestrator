from typing import List, Dict

def update_progress(plan: List[Dict], completed_day: int) -> List[Dict]:
    updated_plan = []

    for item in plan:
        if item["day"] == completed_day:
            item["status"] = "completed"
        else:
            item["status"] = item.get("status", "pending")

        updated_plan.append(item)

    return updated_plan