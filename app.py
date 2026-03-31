# app.py

import streamlit as st
from joke_generator import generate_jokes

st.set_page_config(page_title="Joke App", page_icon="😂")

st.title("😂 Smart Joke Generator")

# UI
topic = st.text_input("Enter Topic", "Dost")

language = st.selectbox(
    "Select Language",
    ["English", "Hindi"]
)

num_jokes = st.slider("Number of Jokes", 1, 5, 2)

# Button
if st.button("Generate 🚀"):

    results = generate_jokes(topic, language, num_jokes)

    output_text = ""

    for i, item in enumerate(results, 1):

        st.markdown(f"### 😂 Joke {i}")
        st.write(item["joke"])

        st.markdown("🧠")
        st.write(item["summary"])


        st.markdown("---")

        # Download text
        output_text += f"Joke {i}:\n{item['joke']}\n"
        output_text += f"Summary {i}:\n{item['summary']}\n"


    # Download button
    st.download_button(
        label="📥 Download Results",
        data=output_text,
        file_name="jokes.txt",
        mime="text/plain"
    )