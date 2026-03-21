import numpy as np
import streamlit as st
from PIL import Image
from tensorflow.keras.models import load_model

model1 = load_model('mask_bestmodel.keras', compile=False)

st.title("Face Mask Detection")

uploaded_file = st.file_uploader('Upload an image: ', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image')

    img = img.resize((128,128))
    img = img.convert('RGB')

    img_arr = np.array(img)/255
    img_arr = img_arr.reshape(1,128,128,3)

    prediction = model1.predict(img_arr)
    score = prediction[0][0]

    if score > 0.65:
        st.success('Approved! The person in the image is wearing a mask 😷')
    else:
        st.error('Warning! The Person in the image is not wearing a mask ⚠️')
        