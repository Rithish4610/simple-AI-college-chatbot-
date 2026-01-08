import os
from dotenv import load_dotenv
import google.generativeai as genai
import json

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load FAQ data
with open("data/college_faq.txt", "r") as f:
    knowledge_base = f.read()

# Save knowledge base
with open("knowledge_base.json", "w") as f:
    json.dump({"content": knowledge_base}, f)

print("✅ Knowledge base stored")
