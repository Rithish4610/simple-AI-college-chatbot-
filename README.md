# 🤖 Simple AI College Chatbot

A simple chatbot built with Streamlit that answers questions about college information.

## Features
- Keyword-based question answering
- Custom knowledge base
- Simple and clean UI

## Setup

1. **Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

2. **Install dependencies**
```bash
pip install streamlit python-dotenv
```

3. **Create knowledge base**
```bash
python ingest.py
```

4. **Run the chatbot**
```bash
streamlit run app.py
```

## Project Structure
```
ai_chatbot/
├── app.py              # Main Streamlit app
├── ingest.py           # Knowledge base creator
├── data/
│   └── college_faq.txt # Your FAQ data
├── .env                # API keys (optional)
└── requirements.txt
```

## Customization
Edit `data/college_faq.txt` to add your own Q&A content.

## License
MIT
