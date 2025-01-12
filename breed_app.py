from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import os
import requests
from sklearn import preprocessing
from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
#from keras.applications.vgg16 import preprocess_input
#from keras.applications.vgg16 import decode_predictions
from PIL import Image
from io import BytesIO
from scipy import ndimage, misc


st.set_page_config(
    page_title="Who let the dogs out?",
    page_icon="🐾"
)

model = load_model('-20-breeds.h5')

breedselection = ['Cocker Spaniel', 'Bloodhound', 'Great Dane', 'Chihuahua', 
                                                'Chow', 'French Bulldog', 'Rottweiler', 'Dachshund', 
                                                'Beagle', 'Doberman', 'Boxer', 'Weimaraner', 
                                                'Toy Terrier', 'Pekinese', 'Siberian Husky', 'Samoyed', 
                                                'Labrador Retriever', 'Collie', 'Golden Retriever', 'Yorkshire Terrier']

st.title("Who let the dogs out?")
st.markdown("A dog breed detection project")

dog_image = st.file_uploader('Add a cute dog here! ⬇', type=['jpg'])

if dog_image:
    if dog_image is not None:
        dogimg = Image.open(dog_image).resize(size=(224, 224))
        st.image(dog_image, width = 300)
        st.write("")
        st.write("Classifying...")
        #dogimg = dog_image.read()
        image1 = np.array(dogimg, dtype=np.float32)
        image = image1.reshape(1,224,224,3)
        result_prob = model.predict(image)
        result = result_prob.argmax(axis=-1)
        le = preprocessing.LabelEncoder()
        result = le.fit_transform(result)
        print("I'm ", str(float(round(np.amax(result_prob)*100,2))), '% sure this cute dog is a ', result[0])
        st.write("I'm ", str(float(round(np.amax(result_prob)*100,2))), "% sure this cute dog is a ", breedselection[np.argmax(result_prob)])
