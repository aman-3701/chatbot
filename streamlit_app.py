import os
import openai
import streamlit as st

# Load API Key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("⚠️ OPENAI_API_KEY not found. Please set it as an environment variable.")
else:
    openai.api_key = api_key

# Streamlit App UI
st.title("🤖 AI Q&A Bot")
st.write("Ask me anything, and I'll try to answer!")

# User Input
question = st.text_input("Your Question:")

if st.button("Get Answer"):
    if not question.strip():
        st.warning("Please enter a question before asking.")
    else:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question}]
            )
            answer = response['choices'][0]['message']['content']
            st.success(answer)
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
