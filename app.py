from src import OllamaClient
import streamlit as st


# Streamed response emulator
def response_generator(prompt, resp_only=True):
    # TODO: refactor if multiple clients
    ollama_client = OllamaClient()
    resp = ollama_client.request(prompt)
    if resp_only:
        return resp['content']
    else:
        return resp


st.title("Simple chat")
st.write("Hello 👋")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
# := means it assign the input and check if it was a truthy value, if not it reaches the else
if user_prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = response_generator(user_prompt)
        response_stream = st.write_stream(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
else:
    if len(st.session_state.messages) > 0:
        st.session_state.messages.append({"role": "assistant", "content": st.write('Enter a valid prompt!')})
