# 🚢 Titanic Data ChatBot

An intelligent chatbot built with **Streamlit**, **Gemini (via Agnos)**, and **SQLite** that lets you ask questions in natural language and receive answers derived from the Titanic dataset — including SQL-powered table queries.

---

## 🌟 Features

- 🔍 Ask natural language questions about Titanic dataset
- 🤖 Gemini API (via Agnos) converts your questions into SQL queries
- 🧠 SQL is executed on an async SQLite database (`aiosqlite`)
- 📊 Results displayed as interactive tables
- 💬 Maintains chat history with code + results
- 🧹 One-click history clear
- ⚡ Fast and responsive with async support

---

## 🧠 How It Works

1. Loads Titanic dataset (`tested.csv`) and inserts into `titanic_async.db`
2. User asks a question like:
   > "How many passengers survived?"
3. Gemini (via Agnos agent) converts the question to SQL
4. SQL is executed via `aiosqlite` on the database
5. Result is returned and shown to user — and saved in chat history

---

## 🚀 Setup Instructions

### 1. Clone this repository
```bash
git clone https://github.com/your-username/titanic-chatbot.git
cd titanic-chatbot


2. Install requirements
bash
Copy
Edit
pip install -r requirements.txt
If you're missing optional dependencies:

bash
Copy
Edit
pip install tabulate aiosqlite pandas streamlit agnos
3. Add your Gemini API key
Edit titanic_chatbot.py and replace this line:

python
Copy
Edit
api_key = "YOUR_GEMINI_API_KEY"
💡 You can get an API key from the Google AI Console.
