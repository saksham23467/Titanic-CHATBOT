


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
````

### 2. Install requirements

```bash
pip install -r requirements.txt
```

If you're missing optional dependencies:

```bash
pip install tabulate aiosqlite pandas streamlit agnos
```

### 3. Add your Gemini API key

Edit `titanic_chatbot.py` and replace this line:

```python
api_key = "YOUR_GEMINI_API_KEY"
```

> 💡 You can get an API key from the [Google AI Console](https://makersuite.google.com/).

---

## 🗃 Dataset

Ensure the file `tested.csv` (Titanic dataset) is in the root directory. If not, download from [Kaggle Titanic](https://www.kaggle.com/competitions/titanic/data) and rename appropriately.

---

## ▶️ Run the App

```bash
streamlit run titanic_chatbot.py
```

The app will launch in your browser at:

```
http://localhost:8501
```

---

## 📦 Requirements

* Python 3.8+
* [Streamlit](https://streamlit.io)
* [Agnos](https://pypi.org/project/agno/)
* [Google Gemini API](https://ai.google.dev/)
* pandas, aiosqlite, tabulate

---

## 📸 Screenshots

| Ask a Question              | Get Results                         |
| --------------------------- | ----------------------------------- |
| ![ask](screenshots/ask.png) | ![results](screenshots/results.png) |

---

## 📂 Project Structure

```
titanic-chatbot/
│
├── titanic_chatbot.py       # Main Streamlit app
├── tested.csv               # Titanic dataset (from Kaggle)
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

---

## 🤝 Credits

* Built by [Your Name](https://github.com/your-username)
* Powered by [Agnos](https://docs.agno.com), [Google Gemini API](https://ai.google.dev/), and [Streamlit](https://streamlit.io)

---

## 📄 License

This project is licensed under the MIT License.

````

---

### ✅ Tip:
Also add a `requirements.txt` with:

```txt
streamlit
pandas
aiosqlite
tabulate
agno
````

Let me know if you want this `README.md` formatted for Hugging Face Spaces or Streamlit Community Cloud instead.
<img width="1465" alt="Screenshot 2025-06-11 at 5 33 32 PM" src="https://github.com/user-attachments/assets/6aee258d-0004-42b1-95f2-659f0ed38374" />

<img width="1421" alt="Screenshot 2025-06-11 at 5 34 58 PM" src="https://github.com/user-attachments/assets/f7449f79-46da-4eb0-a506-bf3068fda1a2" />

