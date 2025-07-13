# File: cli.py
# Entry point for the Agentic AWS Study Coach

import argparse
import sys
import os

# Ensure the project root is in sys.path
base_path = os.path.abspath(os.getcwd())
sys.path.insert(0, base_path)

from agent_core.planner import generate_study_plan
from agent_core.session_coach import run_daily_session
from tools.progress_tracker import load_progress, save_progress

def main():
    parser = argparse.ArgumentParser(description="Agentic AWS Study Coach")
    parser.add_argument("--init", action="store_true", help="Create new study plan")
    parser.add_argument("--today", action="store_true", help="Start today's session")
    parser.add_argument("--quiz", type=str, help="Topic to quiz on (e.g., EC2, IAM)")
    parser.add_argument("--cheatsheet", type=str, help="Generate cheat sheet for a topic")

    args = parser.parse_args()

    if args.init:
        goal = input("📌 Enter your study goal (e.g., 'Prepare for AWS SAA-C03 in 4 weeks'): ")
        hours = input("⏱️ How many hours per day can you study?: ")
        try:
            plan = generate_study_plan(goal, int(hours))
            save_progress(plan)
            print("✅ Study plan initialized and saved.")
        except ValueError:
            print("❌ Please enter a valid number for hours per day.")

    elif args.today:
        try:
            plan = load_progress()
            run_daily_session(plan)
        except FileNotFoundError:
            print("❌ No progress found. Please initialize with --init.")

    elif args.quiz:
        from tools.quiz_generator import quiz_on_topic
        quiz_on_topic(args.quiz)

    elif args.cheatsheet:
        from tools.cheat_sheet import generate_cheatsheet
        generate_cheatsheet(args.cheatsheet)

    else:
        print("ℹ️ Use one of the following options:\n"
              "  --init        Create a new study plan\n"
              "  --today       Start today’s guided session\n"
              "  --quiz TOPIC  Take a quiz on a topic\n"
              "  --cheatsheet TOPIC  Generate a cheat sheet")

if __name__ == "__main__":
    main()
