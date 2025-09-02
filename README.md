# 🤖 AWS-Cert-Agent: Agentic AWS Study Coach (LLM + CLI + Streamlit UI)

**AWS-Cert-Agent** is an open-source Agentic AI study assistant built to help you prepare for AWS certifications like SAA-C03. It supports both a command-line interface (CLI) and a web-based Streamlit UI — powered by a local LLM (TinyLLaMA via [Ollama](https://ollama.com)) or cloud LLMs via [OpenRouter](https://openrouter.ai).

---

## 🧠 What is Agentic AI?

This project is not just another chatbot. It is an **AI Agent** — a system that can:

- ✅ Accept goals (e.g., "Finish AWS prep in 4 weeks")
- ✅ Plan and guide your study sessions
- ✅ Track progress across topics
- ✅ Use tools (quiz generator, cheat sheet maker)
- ✅ Automate actions based on your input

> Agentic AI = **LLM + memory + tools + autonomy**

---

## 🔥 Live Web App (Streamlit Cloud)

▶️ [Click to launch](https://coach-agent-lvsai.streamlit.app/)

---

## 🧩 Features

| Feature               | CLI Support | Web UI |
|----------------------|-------------|--------|
| 📅 Study Plan Generator     | ✅ `--init` | 🔜 (In Progress) |
| 🧠 Daily Study Coach        | ✅ `--today` | 🔜 |
| 🧪 Quiz Generator           | ✅ `--quiz` | ✅ via LLM |
| 📋 Cheat Sheet Generator    | ✅ `--cheatsheet` | ✅ via LLM |
| 💬 Chat with LLM           | ❌ | ✅ |
| 📝 Output Format Selector  | ❌ | ✅ (Text / JSON / YAML / TOML) |
| 📋 Copy & 💾 Download Answer | ❌ | ✅ |
| 🔧 LLM Portability         | ✅ | ✅ |
| 🖥️ Works Offline (Ollama)  | ✅ | ✅ |

---

## 🧱 Project Structure

```
aws-cert-agent/
│
├── agent_core/            # Core agent logic
│   ├── llm_client.py      # Portable LLM wrapper (Ollama/OpenRouter)
│   ├── ollama_client_legacy.py  # (Optional legacy wrapper)
│   ├── planner.py         # Study plan generator
│   ├── session_coach.py   # Daily interactive tutor
│
├── tools/                 # Helper tools
│   ├── quiz_generator.py
│   ├── cheat_sheet.py
│   ├── progress_tracker.py
│
├── data/                  # Local JSON-based memory
│   └── progress.json
│
├── app.py                 # 🌐 Streamlit UI entry point
├── cli.py                 # 🖥️ CLI entry point
├── .env.example           # Environment variable template
├── requirements.txt       # Python dependencies
└── README.md              # You are here!
```

---

## 🧪 How to Run Locally

### ✅ 1. Clone the Repo

```bash
git clone https://github.com/shanmukhkoya/aws-cert-agent.git
cd aws-cert-agent
```

### ✅ 2. Setup LLM Backend

#### Option A: Run Locally with TinyLLaMA

1. Install [Ollama](https://ollama.com)
2. Pull & run the model:

```bash
ollama run tinyllama
```

> The LLM will be accessible at `http://localhost:11434`

#### Option B: Use OpenRouter in the Cloud

1. Create an account at [https://openrouter.ai](https://openrouter.ai)
2. Generate your API key
3. Set it in a `.env` file:

```env
LLM_BACKEND=openrouter
OPENROUTER_API_KEY=your-api-key-here
LLM_MODEL=mistralai/mistral-7b-instruct
```

---

### ✅ 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or generate your own:

```bash
pipreqs . --force
```

---

## 🖥️ Using the CLI

```bash
# Create a personalized study plan
python cli.py --init

# Run today's guided study session
python cli.py --today

# Generate a quiz on an AWS topic
python cli.py --quiz S3

# Get a cheat sheet for any service
python cli.py --cheatsheet EC2
```

---

## 🌐 Using the Streamlit Web App

```bash
streamlit run app.py
```

> Or use the **live version**:
> 📡 [https://aws-cert-agent-lvsai.streamlit.app/](https://aws-cert-agent-lvsai.streamlit.app/)

### 🔥 UI Features

* 📝 Ask AWS questions in plain English
* 🎛️ Choose output format: Text, Markdown, JSON, YAML, TOML
* 📋 One-click copy of answers
* 💾 Download results as file
* 🧠 Powered by your choice of LLM (TinyLLaMA or OpenRouter)

---

## ⚙️ Tech Stack

| Component      | Tech                   |
| -------------- | ---------------------- |
| LLM            | TinyLLaMA / OpenRouter |
| UI             | Streamlit (web), CLI   |
| Agents & Tools | Python modules         |
| Memory         | Local JSON             |
| Deployment     | Streamlit Cloud        |

---

## 📦 .env vs .env.example

* **`.env.example`** = Safe public version (no secrets)
* **`.env`** = Your real API keys (ignored from Git)

Always keep secrets only in `.env` and never commit it.

---

## 🧠 Why Is This Agentic?

✔️ It doesn't just chat.
✔️ It acts on your inputs using real tools and logic.
✔️ It remembers your progress.
✔️ It automates workflows toward a specific goal.

> Agentic AI = **LLM + Tools + Goals + Memory**

You're building the future of how real AI assistants will work.

---

## 🧑‍💻 Author

**Shanmukh Koya**
CTI Solutions Architect | AI Developer
🔗 [LinkedIn](https://www.linkedin.com/in/shanmukhkoya/)
🌐 [GitHub](https://github.com/shanmukhkoya)

---

## 📄 License

[MIT License](LICENSE)

---

## 📌 Future Enhancements

* ✅ UI format controls (done)
* 🔲 Streamlit support for Study Plan & Daily Sessions
* 🔲 Flashcard generator
* 🔲 TUI version with `textual`
* 🔲 RAG support with AWS docs
* 🔲 Cloud file sync for progress.json
