from typing import List, Dict

def create_schedule(plan: List[Dict]) -> List[Dict]:
    schedule = []

    for item in plan:
        day = item["day"]
        topic = item["topic"]

        schedule.append({
            "day": day,
            "topic": topic,
            "time": "10:00 AM - 12:00 PM"
        })

    return schedule