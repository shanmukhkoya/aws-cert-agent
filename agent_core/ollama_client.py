# File: agent_core/ollama_client.py

import requests

def query_ollama(prompt, model="tinyllama"):
    """
    Sends a prompt to Ollama and returns the generated response.
    """
    url = "http://localhost:11434/api/generate"
    try:
        response = requests.post(url, json={
            "model": model,
            "prompt": prompt,
            "stream": False
        })
        response.raise_for_status()
        return response.json()["response"]
    except requests.RequestException as e:
        return f"❌ Ollama request failed: {e}"
