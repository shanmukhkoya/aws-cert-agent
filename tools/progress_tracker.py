# File: tools/progress_tracker.py

import json
import os

PROGRESS_FILE = "data/progress.json"

def save_progress(plan_data: dict):
    """
    Save the entire plan (with updates) to the progress file.
    """
    os.makedirs("data", exist_ok=True)
    with open(PROGRESS_FILE, "w") as f:
        json.dump(plan_data, f, indent=2)

def load_progress() -> dict:
    """
    Load and return the saved plan with progress.
    """
    with open(PROGRESS_FILE, "r") as f:
        return json.load(f)

def mark_complete(plan_data: dict, topic: str):
    """
    Append the completed topic and save.
    """
    if topic not in plan_data["completed"]:
        plan_data["completed"].append(topic)
    save_progress(plan_data)

def get_today_topic(plan_data: dict) -> str:
    """
    Determine the next uncompleted topic in the plan.
    Assumes each topic is listed on a separate line in plan.
    """
    topics = plan_data["plan"].splitlines()

    for line in topics:
        line = line.strip("- ").strip()
        if not line or any(keyword in line.lower() for keyword in ["week", "day", "plan", "goal"]):
            continue
        if line not in plan_data["completed"]:
            return line

    return None
