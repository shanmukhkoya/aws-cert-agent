# File: app.py
import streamlit as st
from agent_core.llm_client import call_llm

st.set_page_config(page_title="AWS Cert Agent", layout="centered")

st.title("🧠 AWSCoach AI")
st.markdown("Your AI study partner for all AWS certifications — ask questions, get explanations, and prepare like a pro.")


# Optional sidebar for LLM details
with st.sidebar:
    st.markdown("### ⚙️ Model Config")
    st.write(f"**Backend:** `{st.session_state.get('LLM_BACKEND', 'openrouter')}`")
    st.write(f"**Model:** `{st.session_state.get('LLM_MODEL', 'meta-llama')}`")
    st.markdown("---")
    st.markdown("🌐 Supports **Ollama** locally and **OpenRouter** in the cloud.")

# User input
prompt = st.text_area("📝 Ask a question (e.g., What is the difference between EC2 and Lambda?)", height=150)

if st.button("🧠 Get Answer"):
    if not prompt.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking like a Solutions Architect..."):
            response = call_llm(prompt)
        st.markdown("### 💡 Answer")
        st.success(response)

st.markdown("---")
st.caption("Built with ❤️ for AWS learners | Powered by Ollama or OpenRouter")
