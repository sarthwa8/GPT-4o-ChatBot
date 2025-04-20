import os
import streamlit as st
import openai
from dotenv import load_dotenv

#configuring openai-api key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print(f"Loaded API Key: {OPENAI_API_KEY}")

#initialise OpenAI client using new SDK

#configuring streamlit page
st.set_page_config(
    page_title="GPT-4o ChatBot",
    page_icon ="🗣️",
    layout = "centered"
)


#initialise chat session in streamlit if not present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#streamlit page title
st.title('📜GPT-4o ChatBot')

#display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


#input field for user's message
user_prompt = st.chat_input("Ask this bot something...")

if user_prompt:
    # add user's message to chat and display
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content":user_prompt})

    #send user's message to gpt.4o and get a response
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                *st.session_state.chat_history
                ]
        )

        assistant_response = response.choices[0].message.content


         # display gpt-4o's response
        with st.chat_message("assistant"):
            st.markdown(assistant_response)

        st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    except Exception as e:
        st.error(f"OpenAI API Error: {e}")








