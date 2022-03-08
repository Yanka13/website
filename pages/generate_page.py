import streamlit as st
import numpy as np
import pandas as pd
from pages import utils
import matplotlib.pyplot as plt
import os
import tensorflow as tf

def app():
    if 'kagglegan_gen.h5' not in os.listdir('models'):
        st.markdown("Please upload model through `Upload model` page!")
    else:
        @st.cache(allow_output_mutation=True)
        def load_model():
            model = tf.keras.models.load_model('models/kagglegan_gen.h5')
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
        #axs.set_title('plots from model')
        st.pyplot(fig)
    
        #st.write('I was clicked 🎉')
        #st.write('Further clicks are not visible but are executed')
    else:
        st.write('I was not clicked 😞')

  
  
        
        
        
        