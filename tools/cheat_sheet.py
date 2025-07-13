# File: tools/cheat_sheet.py

from agent_core.ollama_client import query_ollama

def generate_cheatsheet(topic: str):
    """
    Ask the LLM to summarize the AWS topic in concise bullet points.
    """
    prompt = f"""
Give a concise bullet-point cheat sheet on the AWS topic: {topic}.
Include key definitions, use cases, and any important tips for the exam.
"""
    print("\n📋 Cheat Sheet:\n")
    print(query_ollama(prompt))
