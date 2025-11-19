"""
Assignment 1: AI Question-Answering System
Student: Jimoh-Alabi Islamiat modupeoluwa
Course: Artificial Intelligence
Regno: 250000033
Using: Groq API with Streamlit
"""


import streamlit as st
from groq import Groq
import os
from datetime import datetime

# ============================================
# PAGE CONFIGURATION
# ============================================

st.set_page_config(
    page_title="AI Q&A System",
    page_icon="🤖",
    layout="centered"
)

# ============================================
# TITLE AND DESCRIPTION
# ============================================

st.title("🤖 AI Question-Answering System")
st.markdown("### Ask any question and get an AI-powered answer!")
st.markdown("*Powered by Groq AI - Built for Bioinformatics Assignment 1*")
st.divider()

# ============================================
# API KEY SETUP
# ============================================

# Get API key from environment variable or Streamlit secrets
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except:
        pass

# If no API key found, show input box
if not api_key:
    st.warning("⚠️ No API key found. Please enter your Groq API key below:")
    api_key = st.text_input("Enter Groq API Key", type="password")
    if not api_key:
        st.info("👆 Get your free API key at: https://console.groq.com")
        st.stop()

# Initialize Groq client (fixed for Render compatibility)
try:
    client = Groq(api_key=api_key)
except Exception as e:
    st.error(f"Error initializing Groq client: {e}")
    st.info("Trying alternative initialization...")
    try:
        # Alternative initialization without proxies
        import httpx
        client = Groq(
            api_key=api_key,
            http_client=httpx.Client()
        )
    except Exception as e2:
        st.error(f"Alternative initialization failed: {e2}")
        st.stop()

# ============================================
# LOGGING FUNCTION
# ============================================

def log_interaction(question, answer):
    """Log Q&A interactions to a file."""
    try:
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        log_file = os.path.join(log_dir, "qa_log.txt")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"\n{'='*50}\n")
            f.write(f"Timestamp: {timestamp}\n")
            f.write(f"Question: {question}\n")
            f.write(f"Answer: {answer}\n")
    except:
        pass

# ============================================
# SESSION STATE
# ============================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ============================================
# DISPLAY CONVERSATION HISTORY
# ============================================

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ============================================
# CHAT INPUT
# ============================================

if prompt := st.chat_input("Ask your question here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # Call Groq API
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that answers questions clearly and accurately."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000,
                temperature=0.7
            )
            
            # Extract response
            full_response = response.choices[0].message.content
            
            # Display response
            message_placeholder.markdown(full_response)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
            # Log the interaction
            log_interaction(prompt, full_response)
            
        except Exception as e:
            error_msg = f"Error: {str(e)}\n\nPlease check your API key and internet connection."
            message_placeholder.error(error_msg)

# ============================================
# SIDEBAR WITH INFO
# ============================================

with st.sidebar:
    st.header("ℹ️ About This App")
    st.markdown("""
    **Assignment 1: Q&A System**
    
    This application demonstrates:
    - Integration with LLM API (Groq)
    - Web-based user interface
    - Real-time question answering
    - Conversation history tracking
    
    **How to Use:**
    1. Type your question in the chat box
    2. Press Enter or click Send
    3. Wait for AI response
    4. Continue the conversation!
    
    **Technologies Used:**
    - Python
    - Streamlit
    - Groq API (Llama 3.3)
    """)
    
    st.divider()
    
    # Clear conversation button
    if st.button("🗑️ Clear Conversation"):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    
    # Show conversation count
    st.metric("Total Messages", len(st.session_state.messages))
    
    st.divider()
    
    st.markdown("**Example Questions:**")
    st.markdown("- What is bioinformatics?")
    st.markdown("- Explain DNA sequencing")
    st.markdown("- How does CRISPR work?")

# ============================================
# FOOTER
# ============================================

st.divider()
st.markdown(
    "<p style='text-align: center; color: gray;'>Built with ❤️ for Bioinformatics Masters Program</p>",
    unsafe_allow_html=True
)
