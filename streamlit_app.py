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

# Cover Tab
if selected_tab == "Cover":
    st.title("How to Make Requests?")
    st.write("...without destroying relationships.")

    # Embed HTML and CSS for a static broken heart
    st.markdown(
        """
        <style>
            .heart-container {
                position: relative;
                width: 200px;
                height: 200px;
                margin: auto;
            }

            /* Left piece of the broken heart */
            .left-piece {
                position: absolute;
                width: 100px;
                height: 100px;
                background-color: red;
                transform: rotate(-45deg);
                top: 50px;
                left: 50px;
                clip-path: polygon(0% 0%, 100% 50%, 100% 100%, 0% 100%);
                box-shadow: -3px -3px 5px rgba(0, 0, 0, 0.3); /* Add depth */
            }

            /* Right piece of the broken heart */
            .right-piece {
                position: absolute;
                width: 100px;
                height: 100px;
                background-color: red;
                transform: rotate(-45deg);
                top: 50px;
                left: 150px;
                clip-path: polygon(0% 50%, 100% 0%, 100% 100%, 0% 100%);
                box-shadow: 3px -3px 5px rgba(0, 0, 0, 0.3); /* Add depth */
            }
        </style>

        <div class="heart-container">
            <div class="left-piece"></div>
            <div class="right-piece"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif selected_tab == "Warm-Up":
    # Title of the app
    st.title("Angry Flying Broken Pieces")

    # Description
    st.write("Watch the angry pig image fly in with chaos!")

    # Initialize session state to track the current mode
    if "show_happy_pig" not in st.session_state:
        st.session_state.show_happy_pig = False

    # Button to toggle between modes
    if st.button("Change Image"):
        st.session_state.show_happy_pig = not st.session_state.show_happy_pig

    # Paths to the images
    angry_pig_path = Path("/workspaces/LAMS-pragmatics/images/0$P$-angry.png")
    happy_pig_path = Path("/workspaces/LAMS-pragmatics/images/o$p$.png")

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
                margin: 30px auto;
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

# Raising Awareness Tab
elif selected_tab == "Raising Awareness":
    # Inject CSS to reduce the top margin
    st.markdown(
        """
        <style>
        .css-18e3th9 {
            padding-top: 1rem; /* Reduced top margin */
        }
        .highlight {
            background-color: #ffffcc;
            padding: 5px;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Dropdown to choose between situations
    situation = st.selectbox(
        "Choose a situation:",
        [
            "Situation 1: Loud Talking on a Bus",
            "Situation 2: Spilled Coffee in a Café",
            "Situation 3: Requesting Coins for Coffee",
            "Situation 4: Asking Lecturer to Repeat",
        ],
    )

    # Function to handle request submissions
    def handle_request_submission(selected_requests, request_options):
        if selected_requests:
            st.write("**You selected the following options:**")
            for request in selected_requests:
                st.write(f"- **{request}**")
                st.markdown(
                    f"<div class='highlight'>Comment: {request_options[request]}</div>",
                    unsafe_allow_html=True,
                )
        else:
            st.warning("Please select at least one option before clicking the button.")

    # Situation 1: Loud Talking on a Bus
    if situation == "Situation 1: Loud Talking on a Bus":
        st.write("**Situation 1:** You are on the bus. You are very tired after a hard day at the university. \
                 You are trying to have some rest during the journey. Before you dozed off, a man appeared \
                 and seated next to you. He was talking very loudly on the phone for more than 5 minutes, \
                 disturbing your peace. Choose the option(s) below for the most appropriate response.")

        request_options_1 = {
            "Request 1: Be quiet!": "This response is too direct and may come across as rude.",
            "Request 2: Do you mind lowering the volume?": "This response is polite but slightly informal.",
            "Request 3: Could you lower the volume?": "This is a polite and appropriate way to make a request.",
            "Request 4: Please lower your volume.": "This response is polite and formal, but a bit commanding.",
        }

        request1 = st.checkbox("Request 1: Be quiet!")
        request2 = st.checkbox("Request 2: Do you mind lowering the volume?")
        request3 = st.checkbox("Request 3: Could you lower the volume?")
        request4 = st.checkbox("Request 4: Please lower your volume.")

        if st.button("Submit Situation 1"):
            selected_requests_1 = []
            if request1:
                selected_requests_1.append("Request 1: Be quiet!")
            if request2:
                selected_requests_1.append("Request 2: Do you mind lowering the volume?")
            if request3:
                selected_requests_1.append("Request 3: Could you lower the volume?")
            if request4:
                selected_requests_1.append("Request 4: Please lower your volume.")
            handle_request_submission(selected_requests_1, request_options_1)

    # Situation 2: Spilled Coffee in a Café
    elif situation == "Situation 2: Spilled Coffee in a Café":
        st.write("**Situation 2:** You are sitting in a café enjoying your drink. A waiter accidentally spills \
                 coffee on your table, some of which gets on your clothes. Choose the option(s) below for the \
                 most appropriate response.")

        request_options_2 = {
            "Request 1: Watch where you're going!": "This response is too harsh and might escalate the situation.",
            "Request 2: Could you please clean the table?": "This response is polite and appropriate.",
            "Request 3: Can you offer compensation?": "This response is formal but may seem demanding.",
            "Request 4: It's okay, accidents happen.": "This response is understanding but does not address the issue.",
        }

        request1 = st.checkbox("Request 1: Watch where you're going!")
        request2 = st.checkbox("Request 2: Could you please clean the table?")
        request3 = st.checkbox("Request 3: Can you offer compensation?")
        request4 = st.checkbox("Request 4: It's okay, accidents happen.")

        if st.button("Submit Situation 2"):
            selected_requests_2 = []
            if request1:
                selected_requests_2.append("Request 1: Watch where you're going!")
            if request2:
                selected_requests_2.append("Request 2: Could you please clean the table?")
            if request3:
                selected_requests_2.append("Request 3: Can you offer compensation?")
            if request4:
                selected_requests_2.append("Request 4: It's okay, accidents happen.")
            handle_request_submission(selected_requests_2, request_options_2)

    # Situation 3: Requesting Coins for Coffee
    elif situation == "Situation 3: Requesting Coins for Coffee":
        st.write("**Situation 3:** You want to buy coffee from the vending machine at the university, \
                 but you realize you don’t have enough coins. A classmate or friend is standing nearby. \
                 Choose the option(s) below for the most appropriate response.")

        request_options_3 = {
            "Request 1: Give me some coins!": "This response is too direct and very rude.",
            "Request 2: Could you lend me some coins for coffee?": "This response is polite and friendly.",
            "Request 3: Do you mind sharing some coins with me?": "This response is polite but no promise of returning the coins.",
            "Request 4: Can you spare some coins for coffee, please?": "Polite? Please judge according to your culture.",
        }

        request1 = st.checkbox("Request 1: Give me some coins!")
        request2 = st.checkbox("Request 2: Could you lend me some coins for coffee?")
        request3 = st.checkbox("Request 3: Do you mind sharing some coins with me?")
        request4 = st.checkbox("Request 4: Can you spare some coins for coffee, please?")

        if st.button("Submit Situation 3"):
            selected_requests_3 = []
            if request1:
                selected_requests_3.append("Request 1: Give me some coins!")
            if request2:
                selected_requests_3.append("Request 2: Could you lend me some coins for coffee?")
            if request3:
                selected_requests_3.append("Request 3: Do you mind sharing some coins with me?")
            if request4:
                selected_requests_3.append("Request 4: Can you spare some coins for coffee, please?")
            handle_request_submission(selected_requests_3, request_options_3)

    # Situation 4: Asking Lecturer to Repeat
    elif situation == "Situation 4: Asking Lecturer to Repeat":
        st.write("**Situation 4:** During a university lecture, the lecturer explains an important concept, \
                 but you couldn’t catch what they said. Choose the option(s) below for the most appropriate response(s).")

        request_options_4 = {
            "Request 1: Repeat what you said!": "This response is too direct and may sound rude.",
            "Request 2: Could you please repeat that?": "This response is polite and appropriate.",
            "Request 3: I didn’t quite catch that, could you go over it again?": "This response is polite and shows attentiveness.",
            "Request 4: Sorry, I missed that. Could you clarify, please?": "This response is polite and considerate.",
        }

        request1 = st.checkbox("Request 1: Repeat what you said!")
        request2 = st.checkbox("Request 2: Could you please repeat that?")
        request3 = st.checkbox("Request 3: I didn’t quite catch that, could you go over it again?")
        request4 = st.checkbox("Request 4: Sorry, I missed that. Could you clarify, please?")

        if st.button("Submit Situation 4"):
            selected_requests_4 = []
            if request1:
                selected_requests_4.append("Request 1: Repeat what you said!")
            if request2:
                selected_requests_4.append("Request 2: Could you please repeat that?")
            if request3:
                selected_requests_4.append("Request 3: I didn’t quite catch that, could you go over it again?")
            if request4:
                selected_requests_4.append("Request 4: Sorry, I missed that. Could you clarify, please?")
            handle_request_submission(selected_requests_4, request_options_4)

# Exercises Tab
elif selected_tab == "Exercises":
    st.title("Exercises")
    st.write("This is the Exercises page.")

# Role Play Tab
elif selected_tab == "Role Play":
    st.title("Role Play")
    st.write("This is the Role Play page.")

# References Tab
elif selected_tab == "References":
    st.title("References")
    st.write("Center for Advanced Research on Language Acquisition (CARLA). (n.d.). Strategies for making requests. University of Minnesota. https://archive.carla.umn.edu/speechacts/requests/strategies.html")

# Thank You Tab
elif selected_tab == "Thank You & Questions":
    st.title("Thank You & Questions")
    st.write("Thank you for participating! If you have questions, feel free to ask.")