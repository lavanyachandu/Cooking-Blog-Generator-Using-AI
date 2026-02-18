# 🍽️ AI Driven Cooking Blog Generator

An AI-powered web application that generates high-quality cooking blogs using
**Google Gemini Flash (Latest)**. Built with **Streamlit** and Python.

---

## 🚀 Features

- ✍️ Generate cooking blogs on any topic
- 🤖 Powered by Google Gemini Flash (Latest)
- 📏 Control blog length using a slider
- 😄 Shows a fun programming joke while generating
- 📥 Download generated blog as a `.txt` file
- 🎨 Clean and simple Streamlit UI

---

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** Streamlit
- **AI SDK:** google-genai
- **Model:** `models/gemini-flash-latest`

---

## 📂 Project Structure

AI-DRIVEN-COOKING-BLOG/
│
├── app.py
├── requirements.txt
└── README.md

🔑 API Key Setup (IMPORTANT)

This project uses Google AI Studio (Gemini API).

Recommended (Secure way)

Set API key as environment variable:

setx GOOGLE_API_KEY "YOUR_API_KEY_HERE"


📋 requirements.txt
## ----------------------------------
streamlit
google-genai
## -----------------------------------
Type the following commad in the terminl/Poershell

pip install -r requirements.txt
## --------------------------------------
▶️ Run the Application

streamlit run app.py