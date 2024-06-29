import streamlit as st

st.title('Chatbot')

with st.sidebar:
    st.title("Huggingface Account")
    hf_email = st.text_input('E_mail')
    hf_pass = st.text_input('Password', type='password')

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
