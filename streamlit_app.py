import streamlit as st

# Title of the app
st.title("Image Display with Streamlit")

# Description
st.write("This is a simple app to display an image.")

# Display the image
image_path = "O$P$-angry.png"  # Replace with the path to your image
st.image(image_path, caption="Your Image Caption", use_column_width=True)

# Additional text
st.write("Here is the image you've uploaded!")
