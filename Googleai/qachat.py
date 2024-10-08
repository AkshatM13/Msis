from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai 
import os
import streamlit as st

genai.configure(api_key=os.getenv("Google_Api_Key"))

model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Akshat's LLM Application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input:", key="Input")
submit = st.button("Ask the Question")

if submit and input:
    response = get_gemini_response(input)
    # Add user query and response to session chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader("The Chat history is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")