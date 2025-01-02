# 🧠 Federated Learning for Brain Tumor Detection

Welcome to our project on federated learning for brain tumor detection using MRI scans. This project leverages distributed data across multiple hospitals while preserving data privacy. By utilizing advanced techniques like diffusion models for data augmentation, we aim to improve the accuracy and robustness of tumor detection models.

## 📚 Project Overview

The primary objective of this project is to develop a federated learning system that can detect brain tumors from MRI scans. The system is designed to work with data distributed across various fictional hospitals, ensuring that sensitive medical images remain local and private.

## 📊 Dataset Description

Our dataset is sourced from Kaggle and consists of MRI scans categorized into four types:
- **Glioma Tumors**
- **Meningioma Tumors**
- **Pituitary Tumors**
- **Non-Tumor Cases**

### Original Dataset Structure

- **Total Images**: 7023
- **Training Set**: 5712 images
- **Testing Set**: 1311 images

The dataset is organized into training and testing directories, each containing subdirectories for the four categories.

## 🌟 Diffusion Model for Data Augmentation

To address class imbalance and enhance model performance, we employ a diffusion model to generate synthetic images. This process involves:
- **Generating Synthetic Images**: 25% of the final training dataset consists of these images.
- **Final Training Dataset**: 7616 images after augmentation.

## 📈 Final Preprocessed Dataset

After applying data augmentation using the diffusion model, the final preprocessed dataset consists of a total of 7616 images in the training set. This augmentation helps to balance the dataset and improve the model's ability to generalize across different tumor types. Below is the distribution of images in each category:

- **Glioma Tumors**:
  - Original Images: 1500
  - Augmented Images: 500
  - **Total**: 2000

- **Meningioma Tumors**:
  - Original Images: 1300
  - Augmented Images: 400
  - **Total**: 1700

- **Pituitary Tumors**:
  - Original Images: 1200
  - Augmented Images: 300
  - **Total**: 1500

- **Non-Tumor Cases**:
  - Original Images: 1712
  - Augmented Images: 704
  - **Total**: 2416

The diffusion model helps in creating a more balanced and diverse dataset, which is crucial for training robust machine learning models.

## 🏥 Federated Learning Process

Our federated learning system simulates a network of six fictional hospitals, each acting as a client:
1. **Green Valley Hospital**
2. **Silver Lake Medical Center**
3. **Blue Ridge Health Institute**
4. **Sunnydale Community Hospital**
5. **Maplewood General Hospital**
6. **Riverbend Specialty Clinic**

### Training Rounds

- **Initial Round**: The global model is trained on 10% of the dataset to establish a baseline.
- **Subsequent Rounds**: Clients participate in training rounds, with the number of participating clients varying each round.

### Evaluation Metrics

We use several metrics to evaluate model performance:
- **Accuracy**
- **Precision**
- **Recall**
- **F1 Score**
- **Root Mean Squared Error (RMSE)**
- **Confusion Matrix**

These metrics are calculated after each round to assess both local and global model performance.

## 🖥️ Web Application

The project includes a Streamlit web application that allows users to interact with the federated learning process. Users can:
- View the original and augmented datasets.
- Monitor training metrics and progress.
- Explore the federated learning process and final report.
- Hosted at Streamlit by 

## 🚀 Getting Started

To run the project, follow these steps:
1. Clone the repository from GitHub.
2. Install the required dependencies using `requirements.txt`.
3. Deploy the Streamlit app to explore the project.

## 🤝 Meet the Team

- **Teammate 1**: [Swara Sameer Pawanekar]
- **Teammate 2**: [Neelam Bind]
- **Teammate 3**: [Sahana B R]
