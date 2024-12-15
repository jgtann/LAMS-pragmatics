import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

# Sidebar navigation
st.sidebar.title("Navigation")
selected_tab = st.sidebar.radio(
    "Go to", 
    ["Cover","Diagnostic Activity", "Strategies Activity", "Awareness Activity", "Writing Production Activity", "Speaking Production Activity: 3 Situations", "Summary", "References", "Thank You & Questions"]
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

 # Path to the image
    image_path = "images/broken_heart.png"  # Replace with the actual path to your broken heart image

    # Embed the broken heart image
    st.image(image_path, caption="", use_container_width=True)

# Diagnostic Activity Tab
elif selected_tab == "Diagnostic Activity":
    st.title("Diagnostic Activity")

    # Description
    st.write("Read each situation and make a request as you usually do.")

    # Dropdown to select an image
    image_options = {
        "D1": "images/d1.png",
        "D2": "images/d2.png",
        "D3": "images/d3.png",
    }

    selected_image = st.selectbox(
        "Choose a scenario:",
        list(image_options.keys())
    )

    # Display the selected image
    image_path = image_options[selected_image]
    st.image(image_path, use_container_width=True)

# Strategies Activity Tab
elif selected_tab == "Strategies Activity":
    st.title("Strategies Activity")

    # Description
    st.write("Take a look at the request strategies in the box. \
             Match the strategy that corresponds with sentences 1-6.")

    # Dropdown to select an image
    image_options = {
        "S1": "images/s1.png",
        "S2": "images/s2.png",
    }

    selected_image = st.selectbox(
        "Choose a scenario:",
        list(image_options.keys())
    )

    # Display the selected image
    image_path = image_options[selected_image]
    st.image(image_path, use_container_width=True)

# Awareness Activity Tab
elif selected_tab == "Awareness Activity":
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
        st.write("You are on the bus. You are very tired after a hard day at the university. \
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
        st.write("You are sitting in a café enjoying your drink. A waiter accidentally spills \
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
        st.write("You want to buy coffee from the vending machine at the university, \
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
        st.write("During a university lecture, the lecturer explains an important concept, \
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

# Writing Production Activity Tab

elif selected_tab == "Writing Production Activity":
    st.title("Writing Production Activity")

    # Title
    st.write("Look at the email of a student making a request. Then, label each section.")

    # Embed HTML/CSS/JS using components.html
    components.html(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Drag and Drop</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 20px;
                }
                .container {
                    max-width: 700px;
                    margin: 0 auto;
                }
                .email-container {
                    border: 2px solid #ccc;
                    padding: 10px;
                    background-color: #fafafa;
                    line-height: 1.8;
                    margin-top: 20px;
                }
                .blank {
                    display: inline-block;
                    width: 150px;
                    height: 20px;
                    margin-left: 10px;
                    border: 2px dashed #aaa;
                    text-align: center;
                    font-weight: bold;
                    color: #555;
                    background-color: #f9f9f9;
                    cursor: pointer;
                }
                .labels-container {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 10px;
                    justify-content: center;
                    margin-bottom: 20px;
                }
                .label {
                    background-color: #ffcc99;
                    padding: 5px 10px;
                    border: 1px solid #888;
                    border-radius: 5px;
                    cursor: grab;
                    font-weight: bold;
                }
                .blank.hover {
                    background-color: #e0f7fa;
                    border-color: #00796b;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <!-- Draggable Labels -->
                <div class="labels-container">
                    <div class="label" draggable="true" id="salutation">salutation</div>
                    <div class="label" draggable="true" id="apology">apology</div>
                    <div class="label" draggable="true" id="request">request</div>
                    <div class="label" draggable="true" id="suggestion">suggestion</div>
                    <div class="label" draggable="true" id="consideration">consideration</div>
                    <div class="label" draggable="true" id="closing">closing</div>
                    <div class="label" draggable="true" id="promise">promise</div>
                    <div class="label" draggable="true" id="excuse">excuse</div>
                </div>

                <!-- Email Content -->
                <div class="email-container">
                    <p>Dear Professor, I hope you are doing well. <span class="blank" id="b1"></span></p>
                    <p>I am writing to request for an extension of the assignment due on Monday. <span class="blank" id="b2"></span></p>
                    <p>Unfortunately, I am facing personal issues that are affecting my ability to complete this assignment. <span class="blank" id="b3"></span></p>
                    <p>I apologise for any inconvenience caused. <span class="blank" id="b4"></span></p>
                    <p>I would be grateful if you could extend it until Thursday at the latest to submit the assignment. <span class="blank" id="b5"></span></p>
                    <p>I am committed to submitting a quality assignment that fits the standards established at the beginning of the course. <span class="blank" id="b6"></span></p>
                    <p>Hoping for your kind consideration to my request. <span class="blank" id="b7"></span></p>
                    <p>Sincerely, Student. <span class="blank" id="b8"></span></p>
                </div>
            </div>

            <script>
                const blanks = document.querySelectorAll('.blank');
                const labels = document.querySelectorAll('.label');

                // Add dragstart event to each label
                labels.forEach(label => {
                    label.addEventListener('dragstart', (e) => {
                        e.dataTransfer.setData('text', e.target.id);
                    });
                });

                // Add drop events to blanks
                blanks.forEach(blank => {
                    blank.addEventListener('dragover', (e) => {
                        e.preventDefault();
                        blank.classList.add('hover');
                    });

                    blank.addEventListener('dragleave', () => {
                        blank.classList.remove('hover');
                    });

                    blank.addEventListener('drop', (e) => {
                        e.preventDefault();
                        const draggedLabelId = e.dataTransfer.getData('text');
                        const draggedLabel = document.getElementById(draggedLabelId);

                        if (draggedLabel && !blank.textContent) {
                            blank.textContent = draggedLabel.textContent;
                            draggedLabel.style.display = 'none';
                            blank.classList.remove('hover');
                        }
                    });
                });
            </script>
        </body>
        </html>
        """,
        height=800,
    )

# Speaking Production Activity Tab
elif selected_tab == "Speaking Production Activity: 3 Situations":
    st.title("Speaking Production Activity: 3 Situations")

    # Description
    st.write("In pairs, role-play the presented scenario. \
        Student A acts out Scene A and Student B acts out Scene B. \
            Use the request strategies you have learned.")

    # Dropdown to select an image
    image_options = {
        "Speak Act 1": "images/speakAct1.png",
        "Speak Act 2": "images/speakAct2.png",
        "Speak Act 3": "images/speakAct3.png",
    }

    selected_image = st.selectbox(
        "Choose a scenario:",
        list(image_options.keys())
    )

    # Display the selected image
    image_path = image_options[selected_image]
    st.image(image_path, use_container_width=True)

# Summary Tab
elif selected_tab == "Summary":

    # Title
    st.title("Summary")

    # Path to the image
    image_path = "images/summary_.png"  # Replace with the correct path to your image

    # Helper function to convert local image to base64
    def get_base64_image(image_path):
        with open(image_path, "rb") as image_file:
            base64_str = base64.b64encode(image_file.read()).decode("utf-8")
        return base64_str

    # Import Image to get dimensions
    from PIL import Image

    image = Image.open(image_path)
    width, height = image.size

    # Reduced and enlarged dimensions
    reduced_width = int(width * 0.9)  # Reduce by 10%
    enlarged_width = int(width * 1.2)  # Enlarge by 20%

    # State management for image size
    if "enlarged" not in st.session_state:
        st.session_state.enlarged = False  # Default to reduced size

    # Button to toggle image size
    if st.button("Enlarge Image" if not st.session_state.enlarged else "Reduce Image"):
        st.session_state.enlarged = not st.session_state.enlarged

    # Choose dimensions based on state
    current_width = enlarged_width if st.session_state.enlarged else reduced_width

    # Convert image to Base64 for embedding
    base64_image = get_base64_image(image_path)

    # Embed the image with custom CSS to centralize and resize
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center; margin-top: 20px;">
            <img src="data:image/png;base64,{base64_image}" width="{current_width}" />
        </div>
        """,
        unsafe_allow_html=True,
    )

# References Tab
elif selected_tab == "References":
    st.title("References")
    st.write("Brock, M. N., & Nagasaka, Y. (2005). Teaching Pragmatics in the EFL Classroom? SURE You Can! TESL Reporter, 38(1), 17-26.")
    st.write("Center for Advanced Research on Language Acquisition (CARLA). (n.d.). Strategies for making requests. University of Minnesota. https://archive.carla.umn.edu/speechacts/requests/strategies.html")

# Thank You Tab
elif selected_tab == "Thank You & Questions":
    st.title("Thank You & Questions")
    st.write("Thank you for participating! If you have questions, feel free to ask.")

     # Path to the image
    image_path = "images/QRlink.png"  # Replace with the actual path to your image

    # Embed the image with reduced size and caption
    st.image(image_path, caption="Scan this QR code for link to this website.", width=200)  # Adjust width as needed