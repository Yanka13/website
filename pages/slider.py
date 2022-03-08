import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

def arr2PIL(arr):
    arr = (arr+1)/2*255
    arr = arr.astype('uint8')
    img = Image.fromarray(arr)
    return img

def app():
    #@st.cache(allow_output_mutation=True)
    def load_models(model_list):
        return [tf.keras.models.load_model(model_name) for model_name in model_list]

    #@st.cache(allow_output_mutation=True)
    def get_noise():
        return np.random.normal(0, 1, (32,100))
    
    model_list = ['models/model_gen_epoch_7300.h5', 'models/kagglegan_gen.h5']
    models = load_models(model_list)
    if st.button('GENERATE'):
        noise = get_noise()
        final_model = models[-1]
        final_image = final_model.predict(noise)
        
        col1, col2 = st.columns(2)
        
        col2.image(arr2PIL(final_image[0]),use_column_width=True)

       
        #slider = st.slider('Pick model',0,len(model_list)-1,step=1)
        
        if not slider:
            slider = 0
        print(slider)
        # slider_model = models[slider]
        # slider_image = slider_model.predict(noise)
        # col1.image(arr2PIL(slider_image[0]),use_column_width=True)
if __name__=='__main__':  
    app()