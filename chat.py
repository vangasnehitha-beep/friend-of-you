import streamlit as st
import ollama

st.title("🤖 Friend of You")

question = st.text_input("Ask me anything:")

if st.button("Ask AI"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:

        try:
            response = ollama.chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

            answer = response["message"]["content"]

            st.write("### 🤖 AI Response")
            st.write(answer)

        except Exception as e:
            st.error("Something went wrong:")
            st.code(str(e))