# File: agent_core/session_coach.py

from agent_core.ollama_client import query_ollama
from tools.progress_tracker import get_today_topic, mark_complete

def run_daily_session(plan_data: dict):
    """
    Run a guided session: fetch today's topic, give options, and act based on user's choice.
    """
    topic = get_today_topic(plan_data)

    if not topic:
        print("🎉 All topics completed! You're ready for the exam.")
        return

    print(f"\n📘 Today's Topic: {topic}")
    print("What would you like to do?\n")
    print("  [1] Generate a Cheat Sheet")
    print("  [2] Take a Quiz")
    print("  [3] Mark as Completed")
    print("  [4] Skip for now\n")

    choice = input("Enter your choice [1-4]: ").strip()

    if choice == "1":
        _generate_cheat_sheet(topic)

    elif choice == "2":
        _run_quiz(topic)

    elif choice == "3":
        mark_complete(plan_data, topic)
        print("✅ Topic marked as completed.")

    elif choice == "4":
        print("⏭️ Skipped. You can return to this later.")

    else:
        print("❌ Invalid choice. Try again.")

def _generate_cheat_sheet(topic: str):
    """
    Ask Ollama to create a short cheat sheet for the topic.
    """
    prompt = f"Summarize the AWS topic '{topic}' in bullet points for exam preparation."
    print("\n📋 Cheat Sheet:\n")
    print(query_ollama(prompt))

def _run_quiz(topic: str):
    """
    Ask Ollama to create a quiz for the topic.
    """
    prompt = f"""
Create 3 multiple choice questions on the AWS topic: {topic}.
Each question should have 4 options. Mark the correct option with an asterisk (*).
"""
    print("\n🧠 Quiz:\n")
    print(query_ollama(prompt))
