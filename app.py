import numpy as np
import streamlit as st
from PIL import Image
from tensorflow.keras.models import load_model

# Page Config 
st.set_page_config(
    page_title="Face Mask Detector",
    page_icon="😷",
    layout="centered"
)

# Load Model 
@st.cache_resource
def load_model_cached():
    return load_model('mask_bestmodel.keras', compile=False)

model1 = load_model_cached()

# Header 
st.markdown("<h1>😷 Face Mask Detection</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;'>Upload an image to check if a person is wearing a mask</p>",
    unsafe_allow_html=True
)

# Sidebar 
st.sidebar.title("⚙️ Settings")
threshold = st.sidebar.slider("Detection Threshold", 0.0, 1.0, 0.65)

st.sidebar.markdown("---")
st.sidebar.markdown("### ℹ️ About")
st.sidebar.write("CNN-based Face Mask Detection App")
st.sidebar.write("Built using Streamlit & TensorFlow")

# File Upload 
uploaded_file = st.file_uploader("📤 Upload an image", type=['jpg', 'jpeg', 'png'])

# Prediction 
if uploaded_file is not None:
    img = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.image(img, caption='📷 Uploaded Image', use_container_width=True)

    # Preprocessing
    img_resized = img.resize((128,128)).convert('RGB')
    img_arr = np.array(img_resized) / 255
    img_arr = img_arr.reshape(1,128,128,3)

    with col2:
        st.subheader("🔍 Prediction")

        with st.spinner("Analyzing Image..."):
            prediction = model1.predict(img_arr)
            score = prediction[0][0]

        confidence = score if score > 0.5 else 1 - score

        st.write(f"Confidence: **{confidence*100:.2f}%**")
        st.progress(float(confidence))

        if score > threshold:
            st.success("✅ Mask Detected")
            st.markdown("### 😷 Safe Entry Allowed")
        else:
            st.error("❌ No Mask Detected")
            st.markdown("### ⚠️ Please wear a mask!")
