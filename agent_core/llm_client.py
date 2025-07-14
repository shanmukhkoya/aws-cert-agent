# File: agent_core/llm_client.py
import os
import requests
from dotenv import load_dotenv
import subprocess

load_dotenv()

LLM_BACKEND = os.getenv("LLM_BACKEND", "openrouter")
LLM_MODEL = os.getenv("LLM_MODEL", "openrouter/cinematika")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def call_llm(prompt: str) -> str:
    if LLM_BACKEND == "openrouter":
        return _call_openrouter(prompt)
    elif LLM_BACKEND == "ollama":
        return _call_ollama(prompt)
    else:
        return "[ERROR] Unsupported LLM_BACKEND"

def _call_openrouter(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "https://aws-cert-agent.streamlit.app",
        "X-Title": "AWS Cert Agent"
    }
    payload = {
        "model": LLM_MODEL,
        "messages": [
            {"role": "system", "content": "You are an AWS certification study coach."},
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"[ERROR] OpenRouter API: {response.status_code} - {response.text}"
    except Exception as e:
        return f"[ERROR] OpenRouter request failed: {e}"

def _call_ollama(prompt: str) -> str:
    try:
        result = subprocess.run(
            ["ollama", "run", LLM_MODEL, prompt],
            capture_output=True, text=True
        )
        return result.stdout.strip() if result.returncode == 0 else "[ERROR] Ollama call failed"
    except Exception as e:
        return f"[ERROR] Ollama subprocess failed: {e}"
