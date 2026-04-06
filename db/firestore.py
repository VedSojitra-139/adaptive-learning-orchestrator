import os
from google.cloud import firestore
from dotenv import load_dotenv

load_dotenv()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GCP_CREDENTIALS")

db = firestore.Client()

def save_study_plan(data: dict):
    doc_ref = db.collection("study_plans").document()
    doc_ref.set(data)
    return doc_ref.id

def get_all_plans():
    docs = db.collection("study_plans").stream()

    plans = []
    for doc in docs:
        data = doc.to_dict()
        data["id"] = doc.id
        plans.append(data)

    return plans