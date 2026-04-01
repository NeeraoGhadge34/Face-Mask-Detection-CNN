# 😷 Face Mask Detection System (CNN + Streamlit + Docker + AWS)

🚀 An end-to-end Deep Learning project that detects whether a person is wearing a face mask or not — deployed as a web application with full CI/CD automation.

---

## 📌 Project Overview

This project implements a **Convolutional Neural Network (CNN)** to classify images into:

* 😷 **Mask**
* ❌ **No Mask**

The model is integrated into a **Streamlit web app**, containerized using **Docker**, and deployed on an **AWS EC2 instance** with a **CI/CD pipeline using GitHub Actions**.

---

## 🧠 Key Features

* 📷 Upload image and get real-time prediction
* 📊 Confidence score with visualization
* ⚙️ Adjustable detection threshold
* ⚡ Fast inference using model caching
* 🚀 Fully containerized deployment
* 🔁 Automated CI/CD pipeline

---

## 🏗️ Architecture

```
User → Streamlit App → CNN Model
                  ↓
                Docker
                  ↓
           AWS ECR Repository
                  ↓
            AWS EC2 Instance
                  ↑
        GitHub Actions (CI/CD)
```

---

## 🛠️ Tech Stack

* **Machine Learning:** TensorFlow, Keras
* **Data Processing:** NumPy, OpenCV, Pillow
* **Web App:** Streamlit
* **Deployment:** Docker, AWS EC2
* **CI/CD:** GitHub Actions
* **Language:** Python

---

## 📂 Project Structure

```
Face-Mask-Detection-CNN
│
├── .github/workflows
│   └── main.yaml           # CI/CD workflow
├── app.py                  # Streamlit application
├── best_maskmodel.keras    # Trained CNN model
├── requirements.txt        # Dependencies
├── Dockerfile              # Container configuration
├── README.md               # Project documentation
│
├── test_images/            # Sample images
├── notebook/
│   └── Face_mask_detection.ipynb  # Training notebook
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/NeeraoGhadge34/Face-Mask-Detection-CNN.git
cd Face-Mask-Detection-CNN
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the app locally

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🐳 Docker Setup

### Build Docker Image

```bash
docker build -t mask-detection-app .
```

### Run Container

```bash
docker run -p 8501:8501 mask-detection-app
```

---

## ☁️ AWS Deployment

* Deployed on **AWS EC2 instance**
* Public access via exposed port `8501`
* Docker container runs the Streamlit app

---

## 🔄 CI/CD Pipeline

* Implemented using **GitHub Actions**
* Workflow defined in `.github/workflows/main.yaml`
  
# Automated steps:

Code Push → Build Docker Image → Push to AWS ECR → Deploy on EC2
* 🐳 Docker image is built automatically on every push
* 📦 Image is pushed to Amazon Elastic Container Registry
* 🚀 EC2 instance pulls the latest image and runs the container

---

## 📊 Model Details

* Architecture: Convolutional Neural Network (CNN)
* Input size: `128x128x3`
* Output: Binary classification (Sigmoid)
* Loss: Binary Crossentropy
* Optimizer: Adam

---

## 🧪 Example Output

| Image | Prediction    |
| ----- | ------------- |
| 😷    | Mask Detected |
| ❌     | No Mask       |

---

## 🚀 Future Improvements

* 🔍 Add face detection before classification
* 🎥 Real-time webcam detection
* 📈 Model improvement using transfer learning (MobileNet, ResNet)

---

## 🙌 Acknowledgements

* Dataset: Face Mask Detection Dataset
* Inspired by real-world pandemic safety applications

---

## 📬 Connect with Me

If you liked this project or have suggestions, feel free to connect!

🔗 LinkedIn: *https://www.linkedin.com/in/neerao-ghadge-625329204/*

🔗 GitHub: https://github.com/NeeraoGhadge34

---

⭐ **If you found this project useful, don’t forget to star the repo!**
