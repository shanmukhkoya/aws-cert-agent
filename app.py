# File: app.py
import streamlit as st
from agent_core.llm_client import call_llm

st.set_page_config(page_title="AWS Cert Agent", layout="centered")

st.title("🧠 AWSCoach AI")
st.markdown("Your AI study partner for all AWS certifications — ask questions, get explanations, and prepare like a pro.")

# Sidebar for LLM backend info
with st.sidebar:
    st.markdown("### ⚙️ Model Config")
    st.write(f"**Backend:** `{st.session_state.get('LLM_BACKEND', 'openrouter')}`")
    st.write(f"**Model:** `{st.session_state.get('LLM_MODEL', 'meta-llama')}`")
    st.markdown("---")
    st.markdown("🌐 Supports **Ollama** locally and **OpenRouter** in the cloud.")

# Output format selector
output_format = st.radio("Choose output format:", ["Text", "Markdown", "JSON", "YAML", "TOML"], horizontal=True)

# User prompt input
prompt = st.text_area("📝 Ask a question (e.g., What is the difference between EC2 and Lambda?)", height=100)

if st.button("🧠 Get Answer"):
    if not prompt.strip():
        st.warning("Please enter a question.")
    else:
        # Add formatting instruction to prompt
        full_prompt = f"{prompt}\n\nPlease format the answer as {output_format}."
        with st.spinner("Thinking like a Solutions Architect..."):
            response = call_llm(full_prompt)

        st.markdown("### 💡 Answer")

        # Show response in formatted code block for structured formats
        if output_format.lower() in ["json", "yaml", "toml"]:
            lang = output_format.lower()
            st.code(response.strip(), language=lang)
        elif output_format.lower() == "markdown":
            st.markdown(response)
        else:
            st.success(response)

        # Copy-friendly text input for easy copying
        st.text_area("Copy response", value=response, height=150)

        # Provide download button with appropriate file extension
        ext_map = {"Text": "txt", "Markdown": "md", "JSON": "json", "YAML": "yaml", "TOML": "toml"}
        file_ext = ext_map.get(output_format, "txt")
        filename = f"awscoach_response.{file_ext}"
        st.download_button("💾 Download Response", data=response, file_name=filename, mime="text/plain")

st.markdown("---")
st.caption("Built with ❤️ for AWS learners | Powered by Ollama or OpenRouter")
