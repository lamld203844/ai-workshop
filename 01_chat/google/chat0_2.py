import os
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

convo = model.start_chat()
convo.send_message("Hello, World!")

print(f"Assistant: {convo.last.text.strip()}")