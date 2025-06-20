import streamlit as st
from PIL import Image
import os
import base64
from io import BytesIO

def show_home_page():
    st.set_page_config(page_title="Movie Recommender", layout="wide")

    # Load and encode image
    image_path = os.path.join("assets", "images", "1.jpg")
    image = Image.open(image_path)
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    st.markdown(f"""
        <style>
            .main-container {{
                margin-top: 30px;
                display: flex;
                flex-direction: column;
                align-items: center;
                text-align: center;
            }}

            .welcome-title {{
                font-size: 3.5rem;
                font-weight: 800;
                color: #00BFFF;
                margin-bottom: 10px;
            }}

            .subtext {{
            font-size: 1.3rem;
            color: #dddddd;
            margin: 6px 0;
            font-style: italic;
            font-family: "Raleway", sans-serif;
            }}


            div.stButton > button {{
                background: linear-gradient(135deg, #1e90ff, #00bfff);
                color: white;
                border: none;
                padding: 14px 36px;
                border-radius: 10px;
                font-size: 18px;
                font-weight: 700;
                cursor: pointer;
                transition: all 0.3s ease;
                margin-top: 40px;
            }}

            div.stButton > button:hover {{
                background: linear-gradient(135deg, #63b3ed, #4299e1);
                transform: scale(1.03);
            }}

            .image-wrapper {{
                margin-top: 50px;
                display: flex;
                justify-content: center;
            }}

            .styled-image {{
                width: 70%;
                max-width: 350px;
                border-radius: 20px;
                border: 3px solid #00bfff;
                box-shadow: 0 4px 12px rgba(0, 191, 255, 0.1); /* Softer glow */
                transition: transform 0.3s ease;
            }}

            .styled-image:hover {{
                transform: scale(1.03);
                box-shadow: 0 6px 18px rgba(0, 191, 255, 0.2); /* Slight glow on hover */
            }}

            .footer {{
                text-align: center;
                margin-top: 35px;
                font-size: 16px;
                font-style: italic;
                font-family: "Georgia", "Times New Roman", serif;
                color: #ccc;
                font-weight: 400;
            }}

        </style>

        <div class="main-container">
            <div class="welcome-title">🎬 Welcome to MovieMatch!</div>
            <div class="subtext">Discover movies you'll love with our smart recommendation engine!</div>
            <div class="subtext">Pick your favorite and we'll recommend the perfect next watch.</div>
        </div>
    """, unsafe_allow_html=True)

    # Centered button
    centered_button = st.container()
    with centered_button:
        col1, col2, col3 = st.columns([2, 1, 2])
        with col2:
            if st.button("🚀 Get Started"):
                st.session_state.page = "recommender"

    # Image and footer
    st.markdown(f"""
        <div class="image-wrapper">
            <img src="data:image/png;base64,{img_str}" class="styled-image" alt="Movie image"/>
        </div>
        <div class="footer">
            Made by Susanna John ❤️
        </div>
    """, unsafe_allow_html=True)
