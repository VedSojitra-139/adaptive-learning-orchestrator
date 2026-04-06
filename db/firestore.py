import os
from google.cloud import firestore
from dotenv import load_dotenv
from datetime import datetime

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

def save_workflow_log(log: dict):
    doc_ref = db.collection("workflow_logs").document()
    log["timestamp"] = datetime.utcnow().isoformat()
    doc_ref.set(log)
    return doc_ref.id