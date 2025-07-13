# 🤖 AWS-Cert-Agent: Agentic AWS Study Coach Powered by TinyLLaMA

# 🤖 AWS-Cert-Agent: Agentic AWS Study Coach Powered by TinyLLaMA

This project is an **Agentic CLI Application** that acts as your personalized tutor 
for the **AWS Solutions Architect Associate (SAA-C03)** certification exam. It is 
powered by a local LLM (TinyLLaMA via [Ollama](https://ollama.com)) and built using 
clean, modular Python.

### 🎯 Key Idea

> This is not just an LLM chatbot. This is an **Agent** — it plans, tracks, quizzes, 
> and helps you reach your goal using tools + memory + logic.

---

## 🧠 Features

| Feature               | Description |
|-----------------------|-------------|
| 📅 Study Plan         | Generate a 4-week study plan from your goal |
| 🧠 Daily Tutor        | Guides you through a session based on your current topic |
| 🧪 Quizzes            | Generates AWS topic quizzes (MCQs) |
| 📋 Cheat Sheets       | Summarizes AWS topics in bullet points |
| 🔄 Progress Tracker   | Tracks completed topics and saves progress |
| 🖥️ Fully CLI-Based    | Built for Linux/WSL/local terminal use with TinyLLaMA |

---

## 🧱 Folder Structure

```

aws-cert-agent/
│
├── agent\_core/            # Core agent logic
│   ├── ollama\_client.py   # LLM wrapper for TinyLLaMA
│   ├── planner.py         # Study plan generation agent
│   ├── session\_coach.py   # Daily interactive tutor
│
├── tools/                 # Helper tools for quiz, cheat sheet, progress
│   ├── cheat\_sheet.py
│   ├── quiz\_generator.py
│   ├── progress\_tracker.py
│
├── data/                  # Saved progress
│   └── progress.json
│
├── cli.py                 # 🔥 Main entry point
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

````

---

## 🚀 How to Run Locally

### ✅ 1. Requirements

- Python 3.8+
- pip
- Ollama installed locally: [https://ollama.com](https://ollama.com)

### ✅ 2. Start TinyLLaMA Locally

In a separate terminal:

```bash
ollama run tinyllama
````

This starts the LLM server on `http://localhost:11434`.

> You can also swap this for any Ollama-supported LLM (like llama3, mistral) by editing `ollama_client.py`.

---

### ✅ 3. Clone and Install Dependencies

```bash
git clone https://github.com/shanmukhkoya/aws-cert-agent.git
cd aws-cert-agent
pip install -r requirements.txt
```

> If `requirements.txt` is missing, you can generate it with:
>
> ```bash
> pipreqs . --force
> ```

---

### ✅ 4. Using the Agent via CLI

#### 📌 Create a Study Plan

```bash
python cli.py --init
```

Follow prompts:

* Your goal (e.g., Prepare for AWS SAA-C03 in 4 weeks)
* Daily study hours

#### 📆 Start Today’s Session

```bash
python cli.py --today
```

Get your topic, choose from:

* Cheat Sheet
* Quiz
* Mark as Done
* Skip

#### 🧪 Take a Topic Quiz Anytime

```bash
python cli.py --quiz S3
```

#### 📋 Generate a Topic Cheat Sheet

```bash
python cli.py --cheatsheet EC2
```

---

## ⚙️ Tech Stack

| Component       | Tech Used             |
| --------------- | --------------------- |
| LLM             | TinyLLaMA via Ollama  |
| Interface       | CLI (Python argparse) |
| Storage         | JSON (file-based)     |
| Agent Framework | Custom modular Python |
| Environment     | WSL/Linux Friendly    |

---

## 📁 Sample Output

```
📘 Today's Topic: IAM
What would you like to do?

  [1] Generate a Cheat Sheet
  [2] Take a Quiz
  [3] Mark as Completed
  [4] Skip for now
```

---

## 🧑‍💻 Author

**Shanmukh Koya**
CTI Solutions Architect | AI Developer
🔗 [LinkedIn](https://www.linkedin.com/in/shanmukhkoya/)
🌐 [GitHub](https://github.com/shanmukhkoya)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 💡 Future Enhancements

* ✅ Text UI (TUI) using Textual or Rich
* 🧠 Memory module for topic reflection
* 📊 Session analytics dashboard
* 📚 Flashcard generator
* ☁️ Integration with Notion or AWS SDK

---

## 🧠 Why Is This Agentic?

This is a real agent because it:

* Accepts a goal and acts on it
* Uses a tool (LLM) to make decisions
* Tracks state and adapts behavior
* Automates complex workflows
* Isn’t just replying — it’s **working**

> **This is how modern AI assistants will evolve. You’re building one.**
