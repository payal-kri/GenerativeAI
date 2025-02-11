import streamlit as st
from langchain_groq import ChatGroq
llm=ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    groq_api_key="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"
)
st.title("Simple LLM Chatbot")
st.write("Enter ur query bewlow:")
user_input=st.text_input("Your Ques:", "")
if st.button("Get answer"):
    response=llm.invoke(user_input)
    st.write("### Response")
    st.write(response)

    