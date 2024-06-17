import streamlit as st

# pillow is also know as PIL,
from PIL import Image

st.subheader("Color to Grayscale Converter")

# Create a file uploader component allowing the user to upload a file
uploaded_image = st.file_uploader("Upload Image") 

with st.expander("start camera"):
# start camera
    camera_image= st.camera_input("camera")


if camera_image:

    # create a pillow image instance
    img= Image.open(camera_image)

    # convert the pillow image to grayscale
    gray_img = img.convert("L")
    st.image(gray_img)

if uploaded_image:
    # Open the user uploaded image with PIL
    img = Image.open(uploaded_image)
    # Convert the image to grayscale
    # render the grayscale image on the webpage
    st.image(gray_img)
