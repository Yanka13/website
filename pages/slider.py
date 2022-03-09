import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
from PIL import Image
from .utils import arr2PIL
from .find_k_neighbours import find_k_neighbours
import skimage

# def arr2PIL(arr):
#     arr = (arr+1)/2*255
#     arr = arr.astype('uint8')
#     img = Image.fromarray(arr)
#     return img


def app():
    st.markdown("""# Now it's your turn!""")

    @st.cache(allow_output_mutation=True)
    def load_models(model_list):
        return [tf.keras.models.load_model(model_name) for model_name in model_list]


    def get_noise():
        return np.random.normal(0, 1, (32,100))

    @st.cache(allow_output_mutation=True)
    def get_muatable_list():
        return []


    model_list = ['models/model_epoch_0.h5', 'models/model_epoch_1.h5', 'models/model_epoch_100.h5', 'models/model_epoch_1000.h5', 'models/model_epoch_10000.h5']
    #slider_labels = ['noise', 'epoch 1', 'epoch 100', 'epoch 1000', 'epoch 10000']
    models = load_models(model_list)

    if 'slider' not in st.session_state:
        st.session_state['slider'] = 0

    button = st.button('GENERATE')

    current_noise = get_muatable_list()

    if button or len(current_noise) > 0:
        if button:
           st.session_state['slider'] += 1

        if button and len(current_noise) > 0:
            current_noise.remove(current_noise[0])
        if len(current_noise) == 0:
            current_noise.append(get_noise())

        noise = current_noise[0]
        final_model = models[-1]
        final_image = final_model.predict(noise)

        col1, col2 = st.columns(2)

        col2.image(arr2PIL(final_image[0]),use_column_width=True)
        #model_list_len = len(model_list)-1
        #max = [i for i, v in enumerate(model_list)]
        sliders = st.slider('MODEL SELECTION',0,len(model_list)-1,0,step=1, key=st.session_state['slider'])

        slider_model = models[sliders]
        slider_image = slider_model.predict(noise)
        col1.image(arr2PIL(slider_image[0]),use_column_width=True)
        
        
        with st.container():
            st.write("This is inside the container")
            
            st.title('Find similar images')
            st.write('Encodes images into latent space and finds 4 closest neighbours in that space')

            st.set_option('deprecation.showfileUploaderEncoding', False)

            #uploaded_file = st.file_uploader("Choose an image")

            #if uploaded_file is not None:
                #st.write("Your image:")
            knn_image = (arr2PIL(slider_image[0]))
            #with Image.open(arr2PIL(slider_image[0])) as img:
            resized_img = knn_image.skimage.transform.resize((128, 128))
            st.image(resized_img)
            st.write("Similar images:")

            # find_k_neighbours
            result = find_k_neighbours(image = resized_img, file_location = "data/wikiart_scraped.csv")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                image1 = skimage.io.imread(f"images/abstract_ex/{result[0]['Image_filename']}", as_gray=False)
                st.image(image1)
                st.write(f"{result[0]['Title']}" )
                st.write(f"by {result[0]['Artist']}")

            with col2:
                st.image(f"images/abstract_ex/{result[1]['Image_filename']}")
                st.write(f"{result[1]['Title']}")
                st.write(f"by {result[1]['Artist']}")

            with col3:
                st.image(f"images/abstract_ex/{result[2]['Image_filename']}")
                st.write(f"{result[2]['Title']}")
                st.write(f"by {result[2]['Artist']}")


            with col4:
                st.image(f"raw_data/abstract_ex/{result[3]['Image_filename']}")
                st.write(f"{result[3]['Title']}")
                st.write(f"by {result[3]['Artist']}")


#st.slider('MODEL SELECTION',0,len(model_list)-1,0,step=1, key=st.session_state['slider'])
#models = load_models(list(model_list.values()))
#st.select_slider('MODEL SELECTION', options=slider_labels, value=list(model_list.keys()), key=st.session_state['slider'])
#{'0':'models/model_epoch_0.h5', '1':'models/model_epoch_1.h5', '2':'models/model_epoch_100.h5', '3':'models/model_epoch_1000.h5', '4':'models/model_epoch_10000.h5'}
# if __name__=='__main__':
#     app()
