import streamlit as st
import tensorflow as tf
import streamlit as st
import cv2
import numpy as np
import os
import pandas

from PIL import Image, ImageOps
@st.cache(allow_output_mutation=True)

def load_model():
    model=tf.keras.models.load_model('myMalaria_Model.hdf5')
    return model
with st.spinner('Model is being loaded..'):
    model=load_model()

st.write("""
         # Malaria Parasite Detection
         """
         )



#file = st.text_input("label goes here", default_value_goes_here)

path = st.text_input('image file path')

st.set_option('deprecation.showfileUploaderEncoding', False)

def import_and_predict(image_data, model):
    model1 = model
    img = cv2.imread(image_data)
    img = cv2.resize(img,(128,128))     # resize image to match model's expected sizing
    img = img.reshape(1,128,128,3) # return the image with shaping that TF wants.
    image = np.array(img)
    image = image *(1./255)
    pred = ds_model.predict(image)
    st.image(image, use_column_width=True)
    return pred
    
if path is None:
    st.text("Please enter the path for image file")
else:  
    pred = import_and_predict(path, model)
    if pred>0.5:
        print("The blood cell is uninfected")
    else:
        print("The blood cell is Prasitized")

    
    
    
    



                    
                    
                    
                    
                    
                    