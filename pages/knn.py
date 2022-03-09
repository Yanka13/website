import streamlit as st
from find_k_neighbours import find_k_neighbours
import skimage
import pickle
from tensorflow.keras.models import load_model


st.title('Find similar images')
st.write('Encodes images into latent space and finds 4 closest neighbours in that space')

st.set_option('deprecation.showfileUploaderEncoding', False)

uploaded_file = st.file_uploader("Choose an image")

if uploaded_file is not None:
    st.write("Your image:")
    img = uploaded_file
    st.image(img)
    st.write("Similar images:")

    # find_k_neighbours
    result = find_k_neighbours(image = img, file_location = "data/wikiart_scraped.csv")

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
