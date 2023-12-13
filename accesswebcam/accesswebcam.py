#This access your camera and takes photo and makes it grayscale

import streamlit as st
from PIL import Image

with st.expander("Start Camera"):

    # Start the camera
    camera_image = st.camera_input("Camera")

# Run if Camera Access is allowed
if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

    # Render the image on the webpage
    st.image(gray_img)