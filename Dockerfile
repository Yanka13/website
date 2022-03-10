FROM python:3.8.6-buster

COPY requirements.txt /requirements.txt

COPY data /data
COPY design /design
COPY GIF /GIF
COPY images /images
COPY IMG_OF_GIF /IMG_OF_GIF
COPY models /models
COPY pages /pages
COPY multipage.py /multipage.py
COPY website.py /website.py
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8080

CMD streamlit run website.py –server.port=8080  server.address=0.0.0.0
