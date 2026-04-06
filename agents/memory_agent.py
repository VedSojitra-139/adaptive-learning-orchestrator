from db.firestore import get_all_plans

def retrieve_plans():
    plans = get_all_plans()
    return plans