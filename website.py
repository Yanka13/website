import streamlit as st
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot

add_selectbox = [st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
), st.sidebar.selectbox(
    "test",
    ("ok", "yes", "no"))]

#Title

st.markdown("""# Welcome to the GANdy Warhol project!""")

#How does it work?

st.markdown("""

## How does it work?

GANdy Warhol is a deep learning algorithm which can generate cool abstract expressionism artworks.
Click on the "Generate" button below to see the magic happen...

""")
#load model
@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model('kagglegan_gen.h5')
    return model
model = load_model()

#Generate Button

if st.button('GENERATE'):
    # print is visible in the server output, not in the page
    #print('button clicked!')
    generated_images = model.predict(np.random.normal(0, 1, (32,100)))
    # fig, ax = plt.subplots(figsize=(1, 1))
    # im = ax.imshow(generated_images[0])
    fig, axs = plt.subplots(4, 4, figsize=(11, 11))
    axs[0, 0].imshow(generated_images[0])
    axs[0, 1].imshow(generated_images[1])
    axs[0, 2].imshow(generated_images[2])
    axs[0, 3].imshow(generated_images[3])
    axs[1, 0].imshow(generated_images[4])
    axs[1, 1].imshow(generated_images[5])
    axs[1, 2].imshow(generated_images[6])
    axs[1, 3].imshow(generated_images[7])
    axs[2, 0].imshow(generated_images[8])
    axs[2, 1].imshow(generated_images[9])
    axs[2, 2].imshow(generated_images[10])
    axs[2, 3].imshow(generated_images[11])
    axs[3, 0].imshow(generated_images[12])
    axs[3, 1].imshow(generated_images[13])
    axs[3, 2].imshow(generated_images[14])
    axs[3, 3].imshow(generated_images[15])
    st.pyplot(fig)
    
    #st.write('I was clicked 🎉')
    #st.write('Further clicks are not visible but are executed')
else:
    st.write('I was not clicked 😞')

#GIF Part

st.markdown("""

## Have a look at the algorithm working!

""")

#Comparison with real artwork

st.markdown("""

## Wow, your generated artwork is pretty close to a real one!!

""")

#The project

st.markdown("""

## The project

After 10 superintense weeks at LeWagon, Eloho, YiWen, Saul and Flavien designed this Generative Adversarial Algorithm in 2 weeks.
It has been trained on more than 3,500 images and is now able to create new art pieces.

""")

#Photo of the team

st.markdown("""

## It's us!

""")


CSS = """
h1 {
    color: black;
}
.stApp {
    background-image: url(https://i.insider.com/5501ab9c6da811ed108dbfb3?width=1136&format=jpeg);
    background-size: cover;
}
"""

if st.checkbox('Inject CSS'):
    st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)
