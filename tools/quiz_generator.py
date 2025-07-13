# File: tools/quiz_generator.py

from agent_core.ollama_client import query_ollama

def quiz_on_topic(topic: str):
    """
    Ask the LLM to generate a quiz with multiple choice questions.
    """
    prompt = f"""
Create a short quiz for AWS certification prep on the topic: {topic}.
Include 3 multiple choice questions. Each should have 4 options.
Mark the correct answer with an asterisk (*).
"""
    print("\n🧠 Quiz:\n")
    print(query_ollama(prompt))
