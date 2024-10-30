import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

# Function to get chatbot response using LLaMA 2 model
def getLLamaChatResponse(context):
    # LLaMA 2 model setup
    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens': 200,
                                'temperature': 0.7})

    # Template for chatbot interaction including conversation history
    template = '''
        You are an intelligent AI assistant. Keep the conversation context in mind and respond to the latest user input with concise and helpful replies.
        
        {context}
        Assistant:
    '''
    
    prompt = PromptTemplate(input_variables=['context'], template=template)
    
    # Generate the chatbot's response using invoke instead of __call__
    response = llm.invoke(prompt.format(context=context))
    return response

# Streamlit app configuration
st.set_page_config(page_title="Assistive CHATBOT", layout="centered")

# Title and description
st.title("Assistive CHATBOT 🤖")
st.write("Ask me anything, Let's have a conversation!!")

# Initialize conversation history in session state
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Input field for user's message
with st.form(key='user_input_form'):
    user_input = st.text_input("Enter your message here...", key="user_message", placeholder="Type something...")
    submit = st.form_submit_button("Send")

# Process input and response
if submit and user_input:
    # Append the user's message to the conversation history
    st.session_state.conversation.append(f"User: {user_input}")
    
    # Combine the conversation history into a single context string
    context = "\n".join(st.session_state.conversation)
    
    # Get the assistant's response from the LLaMA model
    response = getLLamaChatResponse(context)
    
    # Append the assistant's response to the conversation history
    st.session_state.conversation.append(f"Assistant: {response}")

# Display the conversation history
for message in st.session_state.conversation:
    st.write(message)
