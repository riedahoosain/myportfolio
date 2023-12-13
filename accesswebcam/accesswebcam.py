# This access your camera and takes photo and makes it grayscale
# This app also can upload and image and convert to grayscale

import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")


#with st.expander("Upload and Image"):
uploaded_image = st.file_uploader("Upload Image")

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

if uploaded_image:
    # Create a pillow image instance
    img = Image.open(uploaded_image)
    gray_img = img.convert("L")
    st.image(gray_img)






