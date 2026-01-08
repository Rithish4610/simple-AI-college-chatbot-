import streamlit as st
import json
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI College Chatbot")
st.title("🤖 College AI Chatbot")

# Load knowledge base
with open("knowledge_base.json", "r") as f:
    data = json.load(f)
    knowledge_base = data["content"]

# Simple keyword-based search
def find_answer(question, kb):
    question = question.lower()
    lines = kb.strip().split('\n')
    
    # Keywords mapping
    keywords = {
        'library': ['library', 'book', 'read'],
        'office': ['office', 'admin', 'administration'],
        'attendance': ['attendance', 'present', 'absent', '75'],
        'exam': ['exam', 'test', 'semester']
    }
    
    for line in lines:
        line_lower = line.lower()
        for key, words in keywords.items():
            if any(word in question for word in words) and any(word in line_lower for word in words):
                return line
    
    return "I don't have information about that. Please ask about library hours, office hours, attendance, or exams."

query = st.text_input("Ask a question")

if query:
    answer = find_answer(query, knowledge_base)
    st.write("### Answer:")
    st.write(answer)
