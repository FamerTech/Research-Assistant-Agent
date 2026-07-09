import os
import streamlit as st
from groq import Groq
import time

# Get API key from environment variable (passed by the Colab notebook)
api_key = os.environ.get('GROQ_API_KEY')
client = Groq(api_key=api_key)

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add an initial system message to set the persona for the assistant
    st.session_state.messages.append({"role": "system", "content":"You are a helpful assistant."})

def chat_with_groq(messages):
  # Call the API with stream=True to get a streaming response
  return client.chat.completions.create(
    model=  "meta-llama/llama-4-scout-17b-16e-instruct",
    messages=messages, # Pass the entire message history for context
    temperature=0.7,
    stream=True
  )

def stream_response(current_messages):
  full_response = ""
  placeholder = st.empty()
  # Iterate over the streamed chunks from the API
  for chunk in chat_with_groq(current_messages):
    if chunk.choices[0].delta.content:
      full_response += chunk.choices[0].delta.content
      # Using st.markdown for potential rich text and adding a blinking cursor
      placeholder.markdown(full_response + "▌")
  placeholder.markdown(full_response) # Display final response without cursor
  return full_response # Return the full response for logging


st.set_page_config(page_title="Chat with Lion AI Assistant", page_icon="🦁", layout="wide")
st.title("Chat with Lion AI Assistant 🦁")

st.write('This is a Research Assistant Agent that uses Groq API to interact with Liama model. You can ask any question and get quick solution')
st.write("___")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    if message["role"] != "system": # Don't display the system message directly to the user
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

user_input = st.chat_input("Type your message here...")

with st.spinner("Generating response..."):
  if user_input:
    # Add user message to chat history and display it
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate and stream assistant response
    with st.chat_message("assistant"):
        assistant_response = stream_response(st.session_state.messages) # Pass the full history
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})

  else:
    # Only show this message if no user input has been provided yet (i.e., only system message in history)
    if len(st.session_state.messages) == 1 and st.session_state.messages[0]["role"] == "system":
        st.write("Please enter a message to start the conversation.")
