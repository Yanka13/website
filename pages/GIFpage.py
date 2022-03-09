import streamlit as st
from PIL import Image
import base64

def app():

    st.title("""Let\'s see some examples of the model running

            """)

    #IMAGES

    image1 = Image.open('IMG_OF_GIF/img_0.png')
    image2 = Image.open('IMG_OF_GIF/img_2.png')
    image3 = Image.open('IMG_OF_GIF/img_4.png')
    image4 = Image.open('IMG_OF_GIF/img_5.png')
    image5 = Image.open('IMG_OF_GIF/img_23.png')

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(image1,use_column_width=True)
        if st.button('GENERATE'):
            file1_ = open("GIF/movie_0.gif", "rb")
            contents1 = file1_.read()
            data_url1 = base64.b64encode(contents1).decode("utf-8")
            st.markdown(f'<img src="data:image/gif;base64,{data_url1}" alt="cat gif">', unsafe_allow_html=True)

    with col2:
        st.image(image2,use_column_width=True)
        if st.button('GENERATE 2'):
            file2_ = open("GIF/movie_2.gif", "rb")
            contents2 = file2_.read()
            data_url2 = base64.b64encode(contents2).decode("utf-8")
            st.markdown(f'<img src="data:image/gif;base64,{data_url2}" alt="cat gif">', unsafe_allow_html=True)

    with col3:
        st.image(image3,use_column_width=True)
        if st.button('GENERATE 3'):
            file3_ = open("GIF/movie_4.gif", "rb")
            contents3 = file3_.read()
            data_url3 = base64.b64encode(contents3).decode("utf-8")
            st.markdown(f'<img src="data:image/gif;base64,{data_url3}" alt="cat gif">', unsafe_allow_html=True)

    with col4:
        st.image(image4,use_column_width=True)
        if st.button('GENERATE 4'):
            file4_ = open("GIF/movie_5.gif", "rb")
            contents4 = file4_.read()
            data_url4 = base64.b64encode(contents4).decode("utf-8")
            st.markdown(f'<img src="data:image/gif;base64,{data_url4}" alt="cat gif">', unsafe_allow_html=True)

    with col5:
        st.image(image5,use_column_width=True)
        if st.button('GENERATE 5'):
            file5_ = open("GIF/movie_23.gif", "rb")
            contents5 = file5_.read()
            data_url5 = base64.b64encode(contents5).decode("utf-8")
            st.markdown(f'<img src="data:image/gif;base64,{data_url5}" alt="cat gif">', unsafe_allow_html=True)
