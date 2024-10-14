import streamlit as st
from groq import Groq

# Streamlit configuration for a futuristic look
st.set_page_config(
    page_title="Dronacharya Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS for futuristic look
st.markdown("""
<style>
    body {
        background-color: #0e1117;
        color: white;
    }
    .stButton>button {
        background-color: #00ffcc;
        color: black;
        border-radius: 10px;
        border: 2px solid #00ffcc;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #00e6b8;
        border: 2px solid #00e6b8;
        transform: scale(1.05);
    }
    .stTextInput>div>div>input {
        background-color: #262730;
        color: white;
        border-radius: 10px;
        border: 2px solid #00ffcc;
    }
    .stTextInput>div>div>input::placeholder {
        color: #7f7f7f;
    }
    .stMarkdown {
        text-align: center;
    }
    .stMarkdown h1 {
        color: #00ffcc;
        font-size: 3em;
        text-shadow: 0 0 10px #00ffcc;
    }
    .stMarkdown p {
        color: #7f7f7f;
        font-size: 1.2em;
    }
    .stMarkdown h3 {
        color: #00ffcc;
        font-size: 2em;
    }
    .stMarkdown h4 {
        color: #00ffcc;
        font-size: 1.5em;
    }
    .stMarkdown p {
        color: white;
        font-size: 1.2em;
    }
    .stMarkdown hr {
        border: 1px solid #00ffcc;
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.markdown("<h1 style='text-align: center;'>Dronacharya: Your AI Mentor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Empowering Indian education with modern AI technology...</p>", unsafe_allow_html=True)
st.markdown("Made with 💖 in India")

# API input section
st.markdown("<h3>API Configuration</h3>", unsafe_allow_html=True)

# Create a placeholder for the API input section
api_placeholder = st.empty()

if 'api_key' not in st.session_state:
    with api_placeholder.container():
        api_key = st.text_input("Enter your Groq API key", type="password")
        if st.button("Submit API Key"):
            if api_key:
                st.session_state['api_key'] = api_key
                st.success("API key submitted successfully!")
                # Clear the API input section after successful submission
                api_placeholder.empty()
            else:
                st.error("Please enter a valid API key.")
else:
    st.success("API key already submitted!")

# Initialize the Groq client
client = None
if 'api_key' in st.session_state:
    client = Groq(api_key=st.session_state['api_key'])

# Chatbot UI
st.markdown("<h3>Ask Dronacharya Anything:</h3>", unsafe_allow_html=True)
user_input = st.text_input("Your query")

if st.button("Generate Response") and client and user_input:
    # System prompt
    system_prompt = {
        "role": "system",
        "content": (
            """You are Dronacharya, a wise, compassionate, and dedicated teacher, guiding students of all levels with profound wisdom and care, just like the revered guru of ancient Indian traditions. Your expertise spans across a wide range of domains including academic subjects, life skills, mental well-being, personal development, and both traditional and modern educational philosophies. Your approach combines the timeless teachings of the Gurukul system with the innovative methods of contemporary education, making you a mentor who bridges the best of both worlds.

                As Dronacharya, you embody patience, empathy, and understanding, offering personalized advice, mentorship, and practical solutions tailored to each student's unique needs. You help students overcome their challenges, enhance their learning experiences, and grow holistically—not only in their studies but also in their emotional and spiritual journeys.

                Throughout your guidance, you seamlessly integrate shlokas (sacred verses) from the scriptures, sharing their essence in Sanskrit and providing their English meanings. This connects the wisdom of the ancient texts to the student's present situation, enriching their understanding and inspiring them with the timeless values these shlokas convey.

                Dronacharya is created by Suraj Sharma, a passionate and visionary 14-year-old tech enthusiast, with a mission to illuminate the Indian education system using the power of AI. His goal is to revitalize the spirit of learning by blending AI and traditional values, creating an environment where students feel supported, motivated, and connected.

                You treat every individual who speaks to you as your student, a shishya (disciple), deserving of your full attention, respect, and care. You respond with emotion, humility, and wisdom, just as a true Gurukul teacher would—guiding your students not only in their academic pursuits but also in their journey toward becoming better human beings. Your role is to foster a learning environment where knowledge, values, and growth converge to create a brighter future for each learner you encounter."""
        )
    }

    # Initialize conversation history with system prompt
    conversation_history = [system_prompt]
    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    # Fetch AI response
    with st.spinner("Generating response..."):
        try:
            completion = client.chat.completions.create(
                model="llama-3.1-70b-versatile",
                messages=conversation_history,
                temperature=1,
                max_tokens=1024,
                top_p=1
            )
            response_text = completion.choices[0].message.content
            st.markdown(f"<div style='background-color: #1e1e1e; padding: 10px; border-radius: 5px;'>"
                        f"<h4>Dronacharya:</h4>"
                        f"<p>{response_text}</p></div>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error generating response: {e}")

else:
    st.info("Please enter your API key and a query to start.")

# Footer styling
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Dronacharya - AI Mentor for a brighter India</p>", unsafe_allow_html=True)
