import streamlit as st
import pandas as pd
import sqlite3
import aiosqlite
import asyncio
from agno.agent import Agent
from agno.models.google import Gemini
from agno.storage.sqlite import SqliteStorage

api_key = "YOUR_API_KEY"

st.set_page_config(page_title="Titanic ChatBot 🚢", layout="wide")
st.title("🚢 Titanic Data ChatBot — Ask Questions from CSV Using Natural Language")

if "agent" not in st.session_state:
    st.session_state.agent = None
if "history" not in st.session_state:
    st.session_state.history = []

@st.cache_data
def load_and_prepare_data():
    df = pd.read_csv("tested.csv")
    conn = sqlite3.connect("titanic_async.db")
    df.to_sql("titanic", conn, if_exists="replace", index=False)
    return df

df = load_and_prepare_data()

async def query_db(sql: str):
    async with aiosqlite.connect("titanic_async.db") as db:
        db.row_factory = aiosqlite.Row
        try:
            async with db.execute(sql) as cursor:
                rows = await cursor.fetchall()
                columns = [col[0] for col in cursor.description]
                return pd.DataFrame(rows, columns=columns)
        except Exception as e:
            return str(e)

async def setup_agent():
    storage = SqliteStorage(table_name="agent_sessions", db_file="tmp/agent.db")

    return Agent(
        model=Gemini(id="gemini-2.0-flash", api_key=api_key),
        instructions=[
            "You're a Titanic dataset expert. Respond with SQL queries when needed.",
            "Only answer questions that can be answered from the Titanic dataset stored in the 'titanic' table.",
            "If asked a natural language question, convert it to an SQL query and return the answer.",
            "NEVER hallucinate. Only use the provided data."
        ],
        storage=storage,
        add_datetime_to_instructions=True,
        add_history_to_messages=True,
        num_history_runs=3,
        markdown=True,
    )

if st.button("🔄 Load Titanic ChatBot"):
    with st.spinner("Setting up agent..."):
        st.session_state.agent = asyncio.run(setup_agent())
    st.success("✅ Chatbot loaded. Ask a question!")

if st.session_state.agent:
    user_input = st.text_input("❓ Ask a question")

    if st.button("💬 Get Answer") and user_input:
        with st.spinner("Thinking..."):
            response = st.session_state.agent.run(user_input)
            response_text = response.content if hasattr(response, "content") else str(response)

            if "```sql" in response_text:
                sql_query = response_text.split("```sql")[1].split("```")[0].strip()
                st.markdown("**🧠 Interpreted SQL:**")
                st.code(sql_query, language="sql")

                try:
                    result_df = asyncio.run(query_db(sql_query))
                    if isinstance(result_df, pd.DataFrame):
                        st.write("📊 **Query Results:**")
                        st.dataframe(result_df)

                        result_markdown = result_df.to_markdown(index=False)
                        chat_response = f"```sql\n{sql_query}\n```\n\n```text\n{result_markdown}\n```"
                    else:
                        st.error(f"SQL Error: {result_df}")
                        chat_response = f"```sql\n{sql_query}\n```\n\n❌ Error:\n{result_df}"
                except Exception as e:
                    st.error(f"SQL Error: {e}")
                    chat_response = f"```sql\n{sql_query}\n```\n\n❌ Error:\n{e}"

            else:
                st.markdown(f"**Bot:** {response_text}")
                chat_response = response_text

            st.session_state.history.append((user_input, chat_response))



    if st.session_state.history:
        with st.expander("🕘 View Chat History", expanded=True):
            for idx, (q, a) in enumerate(st.session_state.history, 1):
                st.markdown(f"**You {idx}:** {q}")
                st.markdown(f"**Bot {idx}:**")
                st.markdown(a)
                st.markdown("---")

        if st.button("🧹 Clear Chat History"):
            st.session_state.history = []
            st.success("Chat history cleared.")
