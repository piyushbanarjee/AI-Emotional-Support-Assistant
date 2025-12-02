# AI-Based-mental-wellbeing-chatbot

AI Supportive Friend (Gemini Powered)
**NOTE: THIS IS JUST A PROTOTYPE/MVP**

HeartTalk is an AI-powered web application that acts as a **supportive virtual friend**. Users can share what is on their mind, and the system responds with empathy, validation, and gentle coping suggestions using the **Google Gemini 2.0 Flash** model.

> ⚠️ **Important Disclaimer:** HeartTalk is **not a medical tool** and does **not replace professional mental health care**. It provides emotional support only.

---

## 📌 Project Objectives

- Provide a safe space for users to express their emotions
- Offer empathetic, non-judgmental AI responses
- Detect crisis-related messages and guide users to real help
- Demonstrate the use of Generative AI for mental health support
- Build a simple, accessible web-based chat interface

---

## ✨ Key Features

- ✅ Empathetic AI chat powered by **Gemini 2.0 Flash**
- ✅ Conversation memory using **Gradio ChatInterface**
- ✅ Crisis keyword detection for self-harm and suicide-related content
- ✅ Real-time responses through a clean web interface
- ✅ Safety-first AI prompt design
- ✅ Lightweight and easy to deploy locally

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| Programming Language | Python 3.9+ |
| AI Model | Google Gemini 2.0 Flash |
| Web Interface | Gradio |
| Environment Management | python-dotenv |
| API SDK | google-generativeai |

---

## 📂 Project Structure

```text
HeartTalk/
│
├── hearttalk_app.py     # Main application file
├── .env                 # Stores Gemini API Key (not uploaded)
├── README.md            # Project documentation
```

---

## 🔑 API Key Configuration

1. Visit **Google AI Studio** and generate a **Gemini API Key**.
2. Create a file named `.env` in the project directory.
3. Add the following line:

```env
GEMINI_API_KEY=your_api_key_here
```

> ⚠️ Never upload your `.env` file to a public repository.

---

## 📦 Installation & Setup

### 1️⃣ Install Dependencies

```bash
pip install gradio google-generativeai python-dotenv
```

---

### 2️⃣ Run the Application

```bash
python hearttalk_app.py
```

After successful execution, open the following link in your browser:

```
http://127.0.0.1:7860
```

---

## 💬 How the System Works

1. The user enters a message in the chat box.
2. The system checks for **crisis-related keywords**.
3. If a crisis is detected:
   - A high-empathy emergency guidance message is displayed.
4. If no crisis is detected:
   - The conversation history is reconstructed.
   - The message is sent to the **Gemini AI model**.
   - The AI replies as a **supportive friend**.
5. **Gradio automatically stores and manages the chat history.**

---

## 🛡️ Crisis Detection Mechanism

The application monitors messages for keywords such as:

- "suicide"
- "kill myself"
- "end my life"
- "hurt myself"
- "no reason to live"
- "overdose"

If detected, the system:
- Responds with empathy
- States its limitations clearly
- Encourages contacting:
  - Trusted people
  - Mental health professionals
  - Local emergency services

---

## 🧠 AI Prompt Engineering

HeartTalk uses a carefully designed **supportive-friend system prompt** that ensures:

- Friendly and conversational tone
- Emotional validation
- No mental health diagnosis
- No medical or medication advice
- Gentle and practical coping suggestions only

---

## ✅ Safety Measures Implemented

- No diagnosis or psychiatric labeling
- No medical or medication suggestions
- Self-harm and violence content handled safely
- Emergency support redirection
- Defensive handling of malformed chat history

---

## 🚀 Future Scope & Enhancements

- 🎤 Voice input using Speech-to-Text
- 🔊 AI speech output using Text-to-Speech
- 📊 Mood tracking and emotion analytics
- ☁️ Cloud deployment
- 📱 Mobile application version
- 🧠 ML-based emotional state classification

---

## ⚠️ Limitations

- Requires internet connectivity
- Keyword-based crisis detection (not ML-based)
- Not real-time voice communication
- Not a substitute for professional therapy

---

## 👨‍💻 Developer Notes

- Chat memory is handled internally by **Gradio ChatInterface**.
- Gemini does not use OpenAI-style role-based messages.
- Manual role simulation is done using:

```text
User: <message>
Friend: <response>
```

- Defensive programming is applied to avoid crashes from malformed history entries.

---

## 📜 License & Usage

This project is created for **academic and demonstration purposes only**. Any form of real-world deployment must comply with:

- Data protection laws
- Mental healthcare regulations
- Ethical AI usage guidelines

---

## ✅ Project Summary

- **Project Title:** HeartTalk – AI Supportive Friend
- **Domain:** Artificial Intelligence / Human-Computer Interaction / Mental Health Support
- **Technology:** Gemini API + Gradio
- **Objective:** Provide a safe, supportive chat environment using Generative AI
