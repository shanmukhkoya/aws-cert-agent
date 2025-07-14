# File: agent_core/ollama_client.py
# ⚠️ LEGACY FILE — Local-only Ollama client
# Retained for local testing with Ollama in WSL
# Not used in production. Use agent_core/llm_client.py instead.


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
