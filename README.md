# AI Question-Answering System

## Artificial intelligence project: Bioinformatics Masters Program

### Description
This is an AI-powered question-answering web application that uses the Groq API (Llama 3.3 model) to provide intelligent responses to user queries. The system features a chat interface with conversation history tracking.

### Technologies Used
- **Python** - Programming language
- **Streamlit** - Web framework for the user interface
- **Groq API** - Large Language Model (Llama 3.3)
- **Git/GitHub** - Version control

### Features
- Real-time question answering using AI
- Conversation history tracking
- Clean and intuitive chat interface
- Persistent conversation within session
- Example questions for guidance

### How to Use
1. Visit the deployed application link
2. Type your question in the chat input box
3. Press Enter or click Send
4. Wait for the AI-generated response
5. Continue asking questions - the conversation history is maintained

### Project Structure
```
.
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
├── .streamlit/
│   ├── secrets.toml      # API keys (not committed to Git)
│   └── config.toml       # Streamlit configuration
└── README.md             # This file
```

### Setup Instructions (For Local Development)
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create `.streamlit/secrets.toml` with your Groq API key
4. Run: `streamlit run app.py`
   
### Deployed on Render: 
https://qa-system-artificial-intelligence-project.onrender.com/


### Author
**Name:** Islamiat Modupeoluwa 
**Program:** Masters in Bioinformatics  
**Course:** Artificial Intelligence 

### Acknowledgments
- Groq for providing the free AI API
- Streamlit for the web framework

### License
Educational project for academic purposes.
