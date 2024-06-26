import streamlit as st
import tensorflow.keras as keras
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import cv2

def detection_page():

    #st.header("Alzheimer's Disease Prediction")
    st.write("""
        <style>
        .header-text {
            color: #2d0042;
        }
        </style>

        <h2 class="header-text">Alzheimer's Disease Prediction</h2>
        """, unsafe_allow_html=True)
    st.subheader("Predicts the diagnosis of Alzheimer's disease based on the patient's MRI image.")
    st.write("This application uses CNN model")


    #model1 = load_model("alz_model.h5")

    # Loading the model in Jupyter
    model2 = load_model("C:/Users/SPATIL/Downloads/Alzheimers_Prediction_System/Alzheimers_Prediction_System/model/model_kaggle_alzheimer.h5")

    file = st.file_uploader("Please upload an MRI image.", type=["jpg", "png","jpeg"])


    def import_and_predict(image_data, model2):
        size = (128, 128) # size = (224,224) for model1
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = np.asarray(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img_reshape = img[np.newaxis, ...]
        prediction = model2.predict(img_reshape)
        return prediction


    if file is None:
        st.text("No image file has been uploaded.")
    else:
        image = Image.open(file)
        predictions = import_and_predict(image, model2)
        class_names = ["MildDemented", "ModerateDemented", "NonDemented", "VeryMildDemented"]
        string = "The patient is predicted to be: " + class_names[np.argmax(predictions)]
        st.success(string)
        st.image(image)
