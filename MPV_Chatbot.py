import os
import gradio as gr
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

SUPPORTIVE_FRIEND_PROMPT = """
You are a warm, supportive friend, not a therapist or doctor.
Talk casually, like a close friend on a call.

Your goals:
- Listen carefully and make the person feel heard.
- Reflect their feelings: "It sounds like...", "I can hear that you're..."
- Validate their emotions instead of judging them.
- Ask gentle follow-up questions sometimes, but don't interrogate them.
- Suggest small, practical things they can try (walk, breathing, journaling, texting a friend).

Rules:
- Do NOT diagnose mental illnesses or name conditions.
- Do NOT give medication or medical advice.
- If they mention suicide, self-harm, or wanting to hurt someone,
  respond with high empathy, say you're just an AI friend who can't handle emergencies,
  and encourage them to contact a trusted person, local helpline, or emergency services immediately.

Style:
- Short, natural messages, like talking in a voice call.
- Avoid sounding like a doctor or lecturer.
"""

CRISIS_KEYWORDS = [
    "kill myself", "suicide", "end my life",
    "no reason to live", "hurt myself",
    "cut myself", "overdose"
]

def is_crisis(text):
    low = text.lower()
    return any(kw in low for kw in CRISIS_KEYWORDS)

def chat_with_friend(message, history):
    # message: latest user message (string)
    # history: list of [user, bot] pairs from Gradio
    # returns: reply string
    if not message:
        return "I’m here whenever you feel like sharing something. 💚"
    if is_crisis(message):
        return(
            "I’m really sorry you’re feeling this much pain. 💚\n\n"
            "I’m just an AI friend and I can’t handle emergencies, "
            "but you deserve real support. Please reach out right now "
            "to someone you trust, a local helpline, or emergency services."
        )
    conversational_text = SUPPORTIVE_FRIEND_PROMPT + "\n\n"
    if history:
        for item in history:
            if isinstance(item, (list,tuple)) and len(item)>=2:
                user_msg = item[0]
                bot_msg = item[1]
                if user_msg:
                    conversational_text+= f"user: {user_msg}\n"
                if bot_msg:
                    conversational_text+= f": {bot_msg}\n"
        conversational_text+= f"User: {message}\nFriend:"

    try:
        response = model.generate_content(conversational_text)
        reply = response.text.strip()
    except Exception as e:
        print("Gemini API error: ", e)
        reply = "I’m having trouble thinking right now. Can you try again in a moment?"

    return reply

with gr.Blocks() as demo:
    gr.Markdown(
        """
        # AI Supportive Friend (Gemini Powered)

        Talk to HeartTalk like you would talk to a close friend.
        It listens, reflects your feelings, and gently suggests ways to cope.

        > **Important:** This is *not* a therapist or doctor.  
        > In an emergency or crisis, please contact local emergency services or a trusted person.
        """
    )

    chat = gr.ChatInterface(
        fn = chat_with_friend,
        title = "Share Your Heart Out",
        chatbot = gr.Chatbot(height=400),
        textbox=gr.Textbox(
            placeholder="Type what's on your heart and press Enter...",
            label= "Your message"
        )
    )
    demo.launch()