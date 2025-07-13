# File: agent_core/planner.py

from agent_core.ollama_client import query_ollama

def generate_study_plan(goal: str, daily_hours: int) -> dict:
    """
    Uses the LLM to generate a 4-week AWS certification study plan.
    Returns a structured dictionary with the goal, hours, and topic breakdown.
    """
    prompt = f"""
You are an expert AWS Solutions Architect certification coach.

A student has the following goal:
- Goal: {goal}
- Daily Study Time: {daily_hours} hour(s)

Create a realistic 4-week study plan for AWS Certified Solutions Architect – Associate (SAA-C03).
Break it into weeks, and list relevant services or concepts to study each week.

Return only the topics in a structured list format.
"""

    print("⏳ Generating study plan using TinyLLaMA...\n")
    response = query_ollama(prompt)

    return {
        "goal": goal,
        "daily_hours": daily_hours,
        "plan": response,
        "completed": []
    }
