import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

# Sidebar navigation
st.sidebar.title("Navigation")
selected_tab = st.sidebar.radio(
    "Go to", 
    ["Cover", "Warm-Up", "Request Lessons", "Raising Awareness", "Exercises", "Role Play", "References", "Thank You & Questions"]
)

# Helper function to convert local image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        base64_str = base64.b64encode(image_file.read()).decode("utf-8")
    return f"data:image/png;base64,{base64_str}"


# Render content for each tab
if selected_tab == "Cover":
    st.title("How to make requests?")
    st.write("...without destroying relationships.")

elif selected_tab == "Warm-Up":
    # Title of the app
    st.title("How to make requests?")

    # Description
    st.write("...without destroying relationships.")

    # Initialize session state to track the current mode
    if "show_happy_pig" not in st.session_state:
        st.session_state.show_happy_pig = False

    # Button to toggle between modes
    if st.button("Click Me!"):
        st.session_state.show_happy_pig = not st.session_state.show_happy_pig

    # Paths to the images
    angry_pig_path = Path("images/0$P$-angry.png")
    happy_pig_path = Path("images/o$p$.png")

    # Convert images to base64
    angry_pig_base64 = get_base64_image(angry_pig_path)
    happy_pig_base64 = get_base64_image(happy_pig_path)

    # Display the images and arrow if "happy pig" mode is active
    if st.session_state.show_happy_pig:
        html_code = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                #container {{
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    gap: 20px;
                }}
                .image {{
                    width: 150px;
                    height: 150px;
                    background-size: cover;
                    background-repeat: no-repeat;
                }}
                .arrow {{
                    font-size: 50px;
                    color: black;
                    margin: 0 10px;
                }}
                #angry-pig {{
                    background-image: url({angry_pig_base64});
                }}
                #happy-pig {{
                    background-image: url({happy_pig_base64});
                }}
            </style>
        </head>
        <body>
            <div id="container">
                <div id="angry-pig" class="image"></div>
                <div class="arrow">➡️</div>
                <div id="happy-pig" class="image"></div>
            </div>
        </body>
        </html>
        """
    else:
        # Display only the angry pig with animation
        html_code = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                #image-container {{
                    position: relative;
                    width: 400px;
                    height: 400px;
                    margin: auto;
                    overflow: hidden;
                    background-color: #d9d9d9;
                    border: 2px solid black;
                }}

                .piece {{
                    position: absolute;
                    opacity: 0;
                    transition: transform 0.3s ease, opacity 0.3s ease; /* Fast chaotic motion */
                }}

                .piece.final {{
                    transition: transform 0.6s cubic-bezier(0.3, 1.5, 0.7, 1), opacity 0.6s ease; /* Settling effect */
                }}
            </style>
        </head>
        <body>
            <div id="image-container"></div>

            <script>
                document.addEventListener("DOMContentLoaded", function () {{
                    const container = document.getElementById('image-container');
                    const imageSrc = "{angry_pig_base64}";  // Embedding the local image
                    const pieceSize = 100; // Size of each piece
                    const rows = Math.ceil(container.clientHeight / pieceSize);
                    const cols = Math.ceil(container.clientWidth / pieceSize);

                    // Create pieces and append them to the container
                    for (let row = 0; row < rows; row++) {{
                        for (let col = 0; col < cols; col++) {{
                            const piece = document.createElement('div');
                            piece.classList.add('piece');
                            piece.style.width = pieceSize + 'px';
                            piece.style.height = pieceSize + 'px';
                            piece.style.backgroundImage = "url(" + imageSrc + ")";
                            piece.style.backgroundPosition = "-" + (col * pieceSize) + "px -" + (row * pieceSize) + "px";
                            piece.style.backgroundSize = (cols * pieceSize) + "px " + (rows * pieceSize) + "px";

                            // Start at random offscreen positions
                            piece.style.transform = "translate(" + (Math.random() * 800 - 400) + "px, " + (Math.random() * 800 - 400) + "px) rotate(" + (Math.random() * 720 - 360) + "deg)";
                            container.appendChild(piece);

                            // Add chaotic movement before settling
                            setTimeout(() => {{
                                piece.style.opacity = 1;
                                piece.style.transform = "translate(" + (Math.random() * 100 - 50) + "px, " + (Math.random() * 100 - 50) + "px) rotate(" + (Math.random() * 90 - 45) + "deg)";
                            }}, Math.random() * 300); // Fast staggered start timing

                            // Final settling into place
                            setTimeout(() => {{
                                piece.classList.add('final');
                                piece.style.transform = "translate(" + (col * pieceSize) + "px, " + (row * pieceSize) + "px) rotate(0deg)";
                            }}, Math.random() * 600 + 600); // Chaotic motion delay
                        }}
                    }}
                }});
            </script>
        </body>
        </html>
        """

    # Embed the HTML into Streamlit
    components.html(html_code, height=450, scrolling=False)

elif selected_tab == "Request Lessons":
    st.title("Request Lessons")

    # Description
    st.write("Here is an illustration related to the lessons. Please take a look.")

    # Option 1: Display the image using st.image
    image_path = Path("images/requestLessons.jpg")  # Replace with your image path
    st.image(image_path, caption="Illustration for Request Lessons", use_container_width=True)

    # Option 2: Display the image using HTML (dynamic embedding)
    image_base64 = get_base64_image(image_path)
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            #lesson-image {{
                width: 100%;
                max-width: 600px;
                margin: 20px auto;
                display: block;
                border: 2px solid black;
                border-radius: 10px;
            }}
        </style>
    </head>
    <body>
        <img id="lesson-image" src="{image_base64}" alt="Request Lessons Image">
    </body>
    </html>
    """
    # Embed the HTML
    components.html(html_code, height=400, scrolling=False)

elif selected_tab == "Raising Awareness":
    st.title("Raising Awareness")
    st.write("Situation 1: \
             You are in the bus. You are very tired after a hard day in the university.\
             You are trying to have some rest in the bus journey.\
             Before you dozed off, a man appeared and seated next to you. \
             He was talking very loudly on the phone for more than 5 minutes, \
             disturbing your peace. Choose the option(s) below for the \
             most appropriate response.")

    # Define lesson options and their corresponding comments
    lesson_options = {
        "Request 1: Be quiet!",
        "Request 2: Do you mind lower down the volume?",
        "Request 3: Could you lower down the volume?",
        "Request 4: Please lower down your volume.",

    }

    # Checkbox options for each lesson
    lesson1 = st.checkbox("Lesson 1: Introduction to Pragmatics")
    lesson2 = st.checkbox("Lesson 2: Politeness Strategies")
    lesson3 = st.checkbox("Lesson 3: Requests and Indirect Speech")
    lesson4 = st.checkbox("Lesson 4: Role of Context in Communication")
    lesson5 = st.checkbox("Lesson 5: Cross-Cultural Pragmatics")

    # Submit button to confirm the selection
    if st.button("Submit"):
        # Collect selected lessons
        selected_lessons = []
        if lesson1:
            selected_lessons.append("Lesson 1: Introduction to Pragmatics")
        if lesson2:
            selected_lessons.append("Lesson 2: Politeness Strategies")
        if lesson3:
            selected_lessons.append("Lesson 3: Requests and Indirect Speech")
        if lesson4:
            selected_lessons.append("Lesson 4: Role of Context in Communication")
        if lesson5:
            selected_lessons.append("Lesson 5: Cross-Cultural Pragmatics")

        # Display comments for selected lessons
        if selected_lessons:
            st.write("**You selected the following lessons:**")
            for lesson in selected_lessons:
                st.write(f"- **{lesson}**")
                st.write(f"  - Comment: {lesson_options[lesson]}")
        else:
            st.warning("Please select at least one lesson before clicking the button.")

elif selected_tab == "Exercises":
    st.title("Exercises")
    st.write("This is the Exercises page.")

elif selected_tab == "Role Play":
    st.title("Role Play")
    st.write("This is the Role Play page.")

elif selected_tab == "References":
    st.title("References")
    st.write("Center for Advanced Research on Language Acquisition (CARLA). (n.d.). Strategies for making requests. University of Minnesota. https://archive.carla.umn.edu/speechacts/requests/strategies.html")

elif selected_tab == "Thank You & Questions":
    st.title("Thank You & Questions")
    st.write("Thank you for participating! If you have questions, feel free to ask.")