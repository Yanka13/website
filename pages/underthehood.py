import streamlit as st
from PIL import Image

st.title('What is going on under the hood?')

st.markdown("""

## What is a Generative Adversarial Network (GAN)?
""")

image = Image.open('../design/GAN explanation.jpeg')
st.image(image, caption='This is a GAN model',use_column_width=True)


st.markdown("""

- GAN models are composed of two models: Generator & Discriminator
- Discriminator is a model which says if an image is fake or real (example: human faces pictures)
- Generator is a model which creates fake images from random noise
- Discriminator trains itself from the training set (real images) to classify either the data is from dataset or not and not to be fooled by a generative model which is learning how to recreate random real images
- They compete with each other and make the generator better at creating real images

""")
