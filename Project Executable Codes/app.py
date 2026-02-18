import streamlit as st
import random
import os
from dotenv import load_dotenv
from google import genai

# --------------------------------
# Load environment variables
# --------------------------------
load_dotenv()

# --------------------------------
# Configure Gemini Client
# --------------------------------
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# --------------------------------
# Random Joke
# --------------------------------
def get_joke():
    jokes = [
        "Why don't programmers like nature? It has too many bugs.",
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "Why did the developer go broke? Because he used up all his cache.",
        "Why was the computer cold? It left its Windows open."
    ]
    return random.choice(jokes)

# --------------------------------
# Blog Generator
# --------------------------------
def recipe_generation(topic, word_count):
    st.write("### 🍳 Generating your content...")
    st.write(f"😄 {get_joke()} 😄")

    prompt = f"""
Write a well-structured cooking blog on the topic:
"{topic}"

Requirements:
- Around {word_count} words
- Clear introduction
- Use headings and subheadings
- Simple and engaging language
- Proper conclusion
"""
    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )

    return response.text

# --------------------------------
# Streamlit UI
# --------------------------------
st.set_page_config(page_title="AI Driven Cooking Blog", layout="centered")

st.title("AI Driven Cooking Blog Generator")

topic = st.text_input("Enter Cooking Blog Topic")
word_count = st.slider("Select Blog Length (words)", 200, 1500, 500)

if st.button("Generate Blog"):
    if topic.strip():
        output = recipe_generation(topic, word_count)
        st.write(output)

        st.download_button(
            label="📥 Download Blog",
            data=output,
            file_name="cooking_blog.txt"
        )
    else:
        st.warning("⚠️ Please enter a topic")
