import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

# Sidebar navigation
st.sidebar.title("Navigation")
selected_tab = st.sidebar.radio(
    "Go to",
    ["Cover", "Warm-Up", "Request Lessons", "Raising Awareness", "Exercises", "Role Play", "References", "Thank You & Questions"],
)

# Helper function to convert local image to base64
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as image_file:
            base64_str = base64.b64encode(image_file.read()).decode("utf-8")
        return f"data:image/png;base64,{base64_str}"
    except FileNotFoundError:
        st.error(f"Image file not found: {image_path}")
        return ""


# Cover Tab
if selected_tab == "Cover":
    st.title("How to make requests?")
    st.write("...without destroying relationships.")

    # Embed HTML, CSS, and JavaScript for the heart-breaking animation
    st.markdown(
        """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                .heart-container {
                    position: relative;
                    width: 200px;
                    height: 200px;
                    margin: auto;
                }

                .heart {
                    position: absolute;
                    width: 100px;
                    height: 100px;
                    background-color: red;
                    transform: rotate(-45deg);
                    top: 50px;
                    left: 50px;
                    animation: break-heart 2s ease forwards;
                }

                .heart::before, .heart::after {
                    content: "";
                    position: absolute;
                    width: 100px;
                    height: 100px;
                    background-color: red;
                    border-radius: 50%;
                }

                .heart::before {
                    top: -50px;
                    left: 0;
                }

                .heart::after {
                    left: 50px;
                    top: 0;
                }

                .left-piece, .right-piece {
                    position: absolute;
                    width: 100px;
                    height: 100px;
                    background-color: red;
                    transform: rotate(-45deg);
                    opacity: 0;
                }

                .left-piece {
                    top: 50px;
                    left: 50px;
                }

                .right-piece {
                    top: 50px;
                    left: 150px;
                }

                @keyframes break-heart {
                    50% {
                        transform: rotate(-45deg) scale(1.1);
                    }
                    100% {
                        transform: rotate(-45deg) scale(0);
                        opacity: 0;
                    }
                }

                @keyframes move-left {
                    0% { opacity: 0; transform: translate(0, 0); }
                    100% { opacity: 1; transform: translate(-100px, 50px); }
                }

                @keyframes move-right {
                    0% { opacity: 0; transform: translate(0, 0); }
                    100% { opacity: 1; transform: translate(100px, 50px); }
                }
            </style>
        </head>
        <body>
            <div class="heart-container">
                <div class="heart" id="heart"></div>
                <div class="left-piece" id="left-piece"></div>
                <div class="right-piece" id="right-piece"></div>
            </div>

            <script>
                setTimeout(() => {
                    const heart = document.getElementById("heart");
                    const leftPiece = document.getElementById("left-piece");
                    const rightPiece = document.getElementById("right-piece");

                    heart.style.display = "none";

                    leftPiece.style.opacity = "1";
                    leftPiece.style.animation = "move-left 2s ease forwards";

                    rightPiece.style.opacity = "1";
                    rightPiece.style.animation = "move-right 2s ease forwards";
                }, 2000);
            </script>
        </body>
        </html>
        """,
        unsafe_allow_html=True,
    )

# Warm-Up Tab
elif selected_tab == "Warm-Up":
    st.title("How to make requests?")
    st.write("...without destroying relationships.")

    # Toggle between Angry Pig and Happy Pig
    if "show_happy_pig" not in st.session_state:
        st.session_state.show_happy_pig = False

    if st.button("Toggle Pig"):
        st.session_state.show_happy_pig = not st.session_state.show_happy_pig

    angry_pig_path = Path("images/0$P$-angry.png")
    happy_pig_path = Path("images/o$p$.png")

    angry_pig_base64 = get_base64_image(angry_pig_path)
    happy_pig_base64 = get_base64_image(happy_pig_path)

    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            .image-container {{
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 20px;
                margin-top: 20px;
            }}

            .image {{
                width: 150px;
                height: 150px;
                background-size: cover;
                background-repeat: no-repeat;
            }}

            #angry {{
                background-image: url({angry_pig_base64});
            }}

            #happy {{
                background-image: url({happy_pig_base64});
            }}
        </style>
    </head>
    <body>
        <div class="image-container">
            <div class="image" id="angry"></div>
            <div class="image" id="happy" style="display: {'block' if st.session_state.show_happy_pig else 'none'};"></div>
        </div>
    </body>
    </html>
    """
    st.components.v1.html(html_code, height=300)

# Raising Awareness Tab
elif selected_tab == "Raising Awareness":
    st.title("Raising Awareness")
    st.markdown("<style>.highlight { background-color: yellow; }</style>", unsafe_allow_html=True)

    situation = st.selectbox("Choose a situation:", ["Situation 1", "Situation 2"])
    if situation == "Situation 1":
        st.write("Situation 1: Loud Talking on the Bus")